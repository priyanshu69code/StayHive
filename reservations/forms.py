from django import forms


class ReservationDetails(forms.Form):
    number_of_guests = forms.ChoiceField(
        choices=[(i, str(i)) for i in range(0, 3)])
    Stay_days = forms.ChoiceField(choices=[(i, str(i)) for i in range(1, 8)])
