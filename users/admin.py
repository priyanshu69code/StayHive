from django.contrib import admin
from users.models import User, Gender, Country, Currency, Language
from django.contrib.auth.admin import UserAdmin

# Register your models here


class CoustomUserAdmin(UserAdmin):
    list_display = ("username", "avatar", "email", "first_name",
                    "last_name", "superhost", "country", "email_verified", "email_secret", "login_method")

    list_filter = ("language", "country", "superhost", "login_method")

    fieldsets = UserAdmin.fieldsets + (
        ('Coustom Fields',
         {'fields': ('gender', 'birthday',
                     "language", "country", "superhost", "bio", "login_method", "avatar")}
         ),
    )


admin.site.register(User, CoustomUserAdmin)
admin.site.register(Gender)
admin.site.register(Language)
admin.site.register(Currency)
admin.site.register(Country)
