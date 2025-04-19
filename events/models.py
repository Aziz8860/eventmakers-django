from django.db import models
from django.contrib.auth.models import User
from core.models import BaseModel

class Event(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    eventDate = models.DateField()
    isDeleted = models.BooleanField(default=False)
    image = models.CharField(max_length=255, blank=True, null=True)
    authorId = models.CharField(max_length=255)
    category = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.name

class Participant(BaseModel):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    eventId = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='participants')
    
    def __str__(self):
        return self.name
