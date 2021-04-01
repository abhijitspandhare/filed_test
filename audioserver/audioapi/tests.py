from django.test import TestCase

# Create your tests here.
from .models import Song, Participants, Podcast
import datetime

class SongTest(TestCase):
    """ Test module for Song model """

    def setUp(self):
        Song.objects.create(
            title='Song 1', duration= 200)
        Song.objects.create(
            title='Song 2', duration= 180)

    def test_puppy_breed(self):
        song1 = Song.objects.get(title='Song 1')
        song2 = Song.objects.get(title='Song 2')
        self.assertEqual(
            song1.__str__(), "Song 1")
        self.assertEqual(
            song2.__str__(), "Song 2")



