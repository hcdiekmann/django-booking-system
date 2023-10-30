from django.db import models

# Create your models here.


class Activity(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='activity_images')
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration_hours = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.price} NZD"


class Booking(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=200)
    customer_email = models.EmailField()
    booking_date = models.DateTimeField()
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.customer_name} - {self.activity.name} - {self.booking_date}"
