from django.contrib import admin
from users.models import User, Gender, Country, Currency, Language
from django.contrib.auth.admin import UserAdmin

# Register your models here


class CoustomUserAdmin(UserAdmin):
    list_display = ("username", "email", "first_name",
                    "last_name", "superhost", "country")
    list_filter = ("language", "country", "superhost")
    fieldsets = UserAdmin.fieldsets + (
        ('Coustom Fields', {'fields': ('gender', 'birthday',
         "language", "country", "superhost", "bio")}),
    )


admin.site.register(User, CoustomUserAdmin)
admin.site.register(Gender)
admin.site.register(Language)
admin.site.register(Currency)
admin.site.register(Country)
