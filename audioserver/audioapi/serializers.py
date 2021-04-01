
from rest_framework import serializers
from .models import Song, Podcast, Audiobook, Participants


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'

class ParticipantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participants
        fields = '__all__'

class AudiobookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audiobook
        fields = '__all__'

class PodcastSerializer(serializers.ModelSerializer):
    participants = serializers.PrimaryKeyRelatedField(queryset=Participants.objects.all(), many=True)
    class Meta:
        model = Podcast
        fields = ('title', 'duration', 'host', 'participants')