from django.contrib import admin
from .models import Movie, Projection, Reservation
# Register your models here.


class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'raiting', 'length', 'genre')
    list_filter = ('genre',)
    search_fields = ['name']


class ProjectionAdmin(admin.ModelAdmin):
    list_display = ('movie_id', 'projection_type', 'projection_time')
    list_filter = ('projection_type',)


class ReservationAdmin(admin.ModelAdmin):
    list_display = ('username', 'projection_id')
    list_filter = ('username',)

admin.site.register(Movie, MovieAdmin)
admin.site.register(Projection, ProjectionAdmin)
admin.site.register(Reservation, ReservationAdmin)
