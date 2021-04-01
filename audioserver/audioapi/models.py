from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=100, blank=False)
    duration = models.PositiveIntegerField(help_text="in seconds", blank=False)
    uploaded_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Participants(models.Model):
    name = models.CharField(max_length=100, blank=False)

class Podcast(models.Model):
    title = models.CharField(max_length=100, blank=False)
    duration = models.PositiveIntegerField(help_text="in seconds", blank=False)
    uploaded_time = models.DateTimeField(auto_now_add=True)
    host =  models.CharField(max_length=100, blank=False)
    participants = models.ManyToManyField(Participants, blank=True)

    def __str__(self):
        return self.title


class Audiobook(models.Model):
    title = models.CharField(max_length=100, blank=False)
    author = models.CharField(max_length=100, blank=False)
    narrator = models.CharField(max_length=100, blank=False)
    duration = models.PositiveIntegerField(help_text="in seconds", blank=False)
    uploaded_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title