from rooms.models import Room
from django.views.generic import ListView
# Create your views here.


class HomeView(ListView):
    model = Room
    template_name = "core/home.html"
    paginate_by = 10
    ordering = "-created_at"
