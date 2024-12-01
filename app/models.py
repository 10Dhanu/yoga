# models.py

from django.db import models
import datetime  # Import datetime to use datetime.date.today

# Define choices at the module level for accessibility across multiple models
SERVICE_CHOICES = [
    ('yoga', 'Yoga'),
    ('meditation', 'Meditation'),
]

LOCATION_CHOICES = [
    ('downtown', 'Downtown'),
    ('online', 'Online'),
]

INSTRUCTOR_CHOICES = [
    ('deepashri', 'Deepashri'),
    # Add other instructors as needed
]

class YogaClass(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    schedule = models.DateTimeField()

    def __str__(self):
        return self.name

class Booking(models.Model):
    service = models.CharField(max_length=50, choices=SERVICE_CHOICES)
    location = models.CharField(max_length=50, choices=LOCATION_CHOICES)
    instructor = models.CharField(max_length=50, choices=INSTRUCTOR_CHOICES)
    date = models.DateField(default=datetime.date.today)  # Set default value
    time = models.TimeField()
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField()
    phone = models.CharField(max_length=20)
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_name} - {self.service} on {self.date} at {self.time}"
