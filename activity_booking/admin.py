from django.contrib import admin
from .models import Activity

# Register your models here.

# make activities modifiable by admin
admin.site.register(Activity)
