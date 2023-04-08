from rest_framework import serializers
from.models import Song

class SongSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title', 'artist', 'album', 'genre', 'likes' ]