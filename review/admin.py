from django.contrib import admin
from review.models import Review
# Register your models here.


class ReviewAdmin(admin.ModelAdmin):
    list_display = ("__str__", "averge_review")


admin.site.register(Review, ReviewAdmin)
