from django import forms
from movies import models


class UploadPosterForm(forms.ModelForm):
    class Meta:
        model = models.Poster
        fields = ['name', 'movie', 'description', "image"]

class AddMovieForm(forms.ModelForm):
    class Meta:
        model = models.Movie
        fields = ['name', 'description', "image"]