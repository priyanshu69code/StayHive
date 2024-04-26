from django import forms
from review import models


class ReviewForm(forms.ModelForm):
    class Meta:
        model = models.Review
        fields = (
            "review",
            "accuracy",
            "communication",
            "clearniness",
            "location",
            "check_in",
            "value",
        )

    def save(self, *args, **kwargs):
        review = super().save(commit=False)
        reservation = kwargs.get("reservation")
        review.room = reservation.room
        review.user = reservation.guest
        reservation.change_reviewed()
        review.save()
        return review
