from django.contrib import admin
from .models import Song, Podcast, Audiobook, Participants

# Register your models here.
admin.site.register(Song)
admin.site.register(Participants)
admin.site.register(Podcast)
admin.site.register(Audiobook)