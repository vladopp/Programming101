from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.


class Movie(models.Model):
    ACTION_STATUS = 'A'
    FANTASY_STATUS = 'F'
    COMEDY_STATUS = 'C'
    DRAMA_STATUS = 'D'
    GENRE_TYPES = (
        (ACTION_STATUS, 'Action'),
        (FANTASY_STATUS, 'Fantasy'),
        (COMEDY_STATUS, 'Comedy'),
        (DRAMA_STATUS, 'Drama')
    )
    name = models.CharField(max_length=100, verbose_name="Movie name")
    raiting = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(10)])
    length = models.PositiveSmallIntegerField()
    genre = models.CharField(max_length=50, choices=GENRE_TYPES)

    def __str__(self):
        return self.name

    def get_genre_display(self):
        for genre in self.GENRE_TYPES:
            if genre[0] == self.genre:
                return genre[1]


class Projection(models.Model):
    _2D = 1
    _3D = 2
    _4D = 3
    IMAX = 4
    IMAX3D = 5
    IMAX4D = 6
    PROJECTION_TYPES = (
        (_2D, '2D'),
        (_3D, '3D'),
        (_4D, '4D'),
        (IMAX, 'IMAX'),
        (IMAX3D, 'IMAX 3D'),
        (IMAX4D, 'IMAX 4D')
    )
    movie_id = models.ForeignKey(Movie)
    projection_type = models.SmallIntegerField(choices=PROJECTION_TYPES)
    # projection_date = models.DateField()
    projection_time = models.DateTimeField()

    def __str__(self):
        return "{} {} {}".format(self.movie_id.name,
                                 self.get_type_display(),
                                 self.projection_time)

    def get_type_display(self):
        for pr_type in self.PROJECTION_TYPES:
            if pr_type[0] == self.projection_type:
                return pr_type[1]


class Reservation(models.Model):
    username = models.CharField(max_length=40)
    projection_id = models.ForeignKey(Projection)
    row = models.PositiveSmallIntegerField()
    column = models.PositiveSmallIntegerField()

    def __str__(self):
        return "Reservation for {} on {}, {}".format(self.username,
                                                     self.row,
                                                     self.column)
