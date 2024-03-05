from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from rooms.models import Room
# Create your views here.


def homepage(request):
    page = request.GET.get("page")
    room_list = Room.objects.all()
    paginator = Paginator(room_list, 10)
    rooms = paginator.get_page(page)
    return render(request, "core/home.html", {"rooms": rooms})
