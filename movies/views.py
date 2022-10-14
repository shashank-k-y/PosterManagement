from django.shortcuts import redirect, render
from django.template import loader
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from movies import forms, models


@login_required
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


@login_required
def image_view(request, pk):
    if request.method == 'GET':
        template = loader.get_template('movies/image_view.html')
        poster = None
        try:
            poster = models.Poster.objects.get(id=pk)
        except ObjectDoesNotExist:
            messages.info(request, "No movies to display")

        if request.user not in poster.permitted_viewers.all() and poster not in request.user.posters.all(): # noqa
            messages.info(request, "you dont have access to this Image.")

        context = {
            'poster': poster,
        }
    return HttpResponse(template.render(context, request))


@login_required()
def index(request):
    template = loader.get_template('movies/posters.html')
    user_uploaded_poster = models.Poster.objects.filter(uploader=request.user)
    accessable_posters = request.user.poster_set.all()
    context = {
        'all_posters': accessable_posters if accessable_posters.exists() else None, # noqa
        'user_uploaded_posters': user_uploaded_poster
    }
    return HttpResponse(template.render(context, request))


@login_required
def upload_poster(request):
    if request.method == 'POST':
        form = forms.UploadPosterForm(request.POST, request.FILES)

        if form.is_valid():
            user = request.user
            form.cleaned_data.update(uploader=user)
            models.Poster.objects.create(**form.cleaned_data)
            return redirect(to='home')
    else:
        form = forms.UploadPosterForm()
    context = {'form': form}
    return render(request, 'movies/upload_poster.html', context=context)

@login_required
def add_movie(request):
    if request.method == 'POST':
        form = forms.AddMovieForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect(to='list')
    else:
        form = forms.AddMovieForm()
    context = {'form': form}
    return render(request, 'movies/add_movie.html', context=context)
