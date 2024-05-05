from rest_framework import serializers
from .models import Albom,Artist,Song

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ("name", "image", "last_update", "created_date")

class AlbomSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(read_only=True)
    class Meta:
        model = Albom
        fields = ("title", "artist", "image", "last_update", "created_date")

class SongSerializer(serializers.ModelSerializer):
    albom = AlbomSerializer(read_only=True)
    class Meta:
        model = Song
        fields = ("title", "albom", "image", "last_update", "created_date")
