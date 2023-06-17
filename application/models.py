from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=60)
    genre = models.CharField(max_length=60)
    duration = models.IntegerField(validators=[MinValueValidator(0)])
    score = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(10)
        ]
    )

    def __str__(self):
        return self.name


class Showtime(models.Model):
    film_name = models.CharField(max_length=60)
    date = models.DateTimeField(auto_now=True)


class Booking(models.Model):
    showtime_id = models.IntegerField(
        default=1,
        validators=[MinValueValidator(0)]
    )
    count = models.IntegerField(default=1, validators=[MinValueValidator(0)])
