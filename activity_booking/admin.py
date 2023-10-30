from django.contrib import admin
from .models import Activity, Booking

# Register your models here.

# make modifiable by admin
admin.site.register(Activity)
admin.site.register(Booking)