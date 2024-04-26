from django.shortcuts import render
# imprort the createview
# Create your views here.
from reservations import models as reservation_models
from . import forms
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def create_review(request, reservation_pk):
    reservation = reservation_models.Reservation.objects.get_or_none(
        pk=reservation_pk)
    if request.method == "POST" and request.user == reservation.guest:
        form = forms.ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(reservation=reservation)
            messages.success(request, "Review created")
            return redirect(reverse("reservations:detail", kwargs={"pk": reservation.pk, }))
        else:
            messages.error(
                request, "The Numerical value should be between 1 and 5")
            return render(request, "review/review_form.html", {"form": form})
    else:
        messages.error(request, "Can't review")
        return redirect(reverse("core:home"))
