from rest_framework import serializers

from .models import Movie, Showtime, Booking


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = ('name', 'genre', 'duration', 'score')


class ShowtimeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Showtime
        fields = ('film_name', 'date')


class BookingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Booking
        fields = ('showtime_id', 'count')
