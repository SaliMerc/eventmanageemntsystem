from django.db import models

from django.contrib.auth.hashers import make_password, check_password
# Create your models here.
# Task:
# Create an application for managing events

# 1. In models have a class 'Event'. Fields can  include name, description, location, start_time, end_time, and organizer.

# 2. Also a second class 'Participant:' Fields can include name, email, and event (ForeignKey to Event).

# 3. To allow the app to take user input in regards to events and  participants, Create forms for event creation and participant registration.

# 4. For CRUD Operations, make sure you Add functionality to create, update, and delete events. Also, allow participants to register for events and view event details.
class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    organizer = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Participant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    def __str__(self):
        return self.name


