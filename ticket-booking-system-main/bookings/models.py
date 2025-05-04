from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    venue = models.CharField(max_length=100)
    description = models.TextField()
    total_seats = models.PositiveIntegerField()
    available_seats = models.PositiveIntegerField()
    image_url = models.URLField(blank=True)

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    num_seats = models.PositiveIntegerField()
    booked_at = models.DateTimeField(auto_now_add=True)