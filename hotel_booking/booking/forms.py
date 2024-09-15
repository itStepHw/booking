from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Room, Booking


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['room_number', 'room_type', 'price_per_night', 'description', 'photo']


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['room', 'check_in', 'check_out']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Используем виджет DateInput с атрибутом type="date"
        self.fields['check_in'].widget = forms.DateInput(attrs={'type': 'date'})
        self.fields['check_out'].widget = forms.DateInput(attrs={'type': 'date'})