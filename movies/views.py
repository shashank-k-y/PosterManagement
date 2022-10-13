from django.template import loader
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages

from movies import models


def movie_list_view(request):

    if request.method == 'GET':
        template = loader.get_template('movies/movie_list.html')
        movies = models.Movie.objects.all()
        if not movies:
            messages.info(request, "No movies to display")

        context = {
            'movies': movies,
        }
    return HttpResponse(template.render(context, request))


def image_view(request, pk):
    if request.method == 'GET':
        template = loader.get_template('movies/image_view.html')
        movie = None
        try:
            movie = models.Movie.objects.get(id=pk)
        except ObjectDoesNotExist:
            messages.info(request, "No movies to display")

        context = {
            'movie': movie,
        }
    return HttpResponse(template.render(context, request))
