from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View

from movies.models import Movie


class MoviesView(View):
    def get(self, request):
        movies = Movie.objects.all()
        return render(request, "movies/movie_list.html", {"movie_list": movies})
