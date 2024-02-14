from django.contrib import admin
from lists.models import List

# Register your models here.


class ListAdmin(admin.ModelAdmin):
    list_display = ("__str__", "user", "count_rooms",)

    search_fields = ("name",)


admin.site.register(List, ListAdmin)
