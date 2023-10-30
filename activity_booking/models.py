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
    
