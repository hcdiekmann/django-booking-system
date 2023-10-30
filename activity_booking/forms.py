from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['activity', 'customer_name', 'customer_email', 'booking_date']