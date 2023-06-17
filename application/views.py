
from rest_framework import generics, response

from .serializers import MovieSerializer, ShowtimeSerializer, BookingSerializer
from .models import Movie, Showtime, Booking


class MovieViewSet(generics.ListAPIView):
    queryset = Movie.objects.all().order_by('name')
    serializer_class = MovieSerializer


class ShowtimeViewSet(generics.ListAPIView):
    queryset = Showtime.objects.all().order_by('date')
    serializer_class = ShowtimeSerializer


class BookingViewSet(generics.CreateAPIView):
    serializer_class = BookingSerializer

    def post(self, request, *args, **kwargs):
        showtime_id = request.POST.get('showtime_id')
        count = request.POST.get('count')
        print(showtime_id, count)
        if count and showtime_id:
            try:
                showtime = Showtime.objects.get(id=showtime_id)
            except Exception:
                return response.Response('', '505')
            booking = Booking(showtime_id=showtime.id, count=count)
            booking.save()
            return response.Response('', '200')
        else:
            return response.Response('', '505')
