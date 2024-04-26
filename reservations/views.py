import datetime
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.views.generic import View
from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from rooms import models as room_models
from . import models
from django.http import Http404
from review import forms as review_forms
from .forms import ReservationDetails


def reservationExtraDetails(request, room, year, month, day):
    form = ReservationDetails(request.POST)
    if request.method == "POST":
        form = ReservationDetails(request.POST)
        if form.is_valid():
            number_of_guests = form.cleaned_data.get("number_of_guests")
            Stay_days = form.cleaned_data.get("Stay_days")
            return redirect(
                reverse(
                    "reservations:create",
                    kwargs={
                        "room": room,
                        "year": year,
                        "month": month,
                        "day": day,
                        "stays": Stay_days,
                        "guests": number_of_guests,
                    },
                )
            )
    return render(request, "reservations/reservation_details.html", {"form": form})

    # Create your views here.


class CreateError(Exception):
    pass


@login_required
def create(request, room, year, month, day, stays, guests):
    try:
        date_obj = datetime.datetime(year, month, day)
        room = room_models.Room.objects.get(pk=room)
        models.BookedDay.objects.get(day=date_obj, reservation__room=room)
        raise CreateError()
    except (room_models.Room.DoesNotExist, CreateError):
        messages.error(request, "Can't reserve that room")
        return redirect(reverse("core:home"))
    except models.BookedDay.DoesNotExist:
        reservation = models.Reservation.objects.create(
            guest=request.user,
            room=room,
            check_in=date_obj,
            check_out=date_obj + datetime.timedelta(days=stays-1),
            number_of_guests=guests,
        )
        return redirect(reverse("reservations:detail", kwargs={"pk": reservation.pk}))


class ReservationDetailView(View):
    def get(self, *args, **kwargs):
        pk = kwargs.get("pk")
        reservation = models.Reservation.objects.get_or_none(pk=pk)
        if not reservation or (
            reservation.guest != self.request.user
            and reservation.room.host != self.request.user
        ):
            raise Http404()
        form = review_forms.ReviewForm()
        return render(
            self.request,
            "reservations/detail.html",
            {"reservation": reservation, "form": form},
        )


@login_required
def edit_reservation(request, pk, verb):
    reservation = models.Reservation.objects.get_or_none(pk=pk)
    if not reservation or (
        reservation.guest != request.user
        and reservation.room.host != request.user
    ):
        raise Http404()
    if verb == "confirm":
        reservation.status = models.Reservation.STATUS_CONFIRMED
    elif verb == "cancel":
        reservation.status = models.Reservation.STATUS_CANCELED
        booked_days = models.BookedDay.objects.filter(
            reservation=reservation).delete()
        print(booked_days)
    reservation.save()
    messages.success(request, "Reservation updated")
    return redirect(reverse("reservations:detail", kwargs={"pk": reservation.pk}))
