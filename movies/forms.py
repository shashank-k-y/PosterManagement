from django import forms
from movies import models


class UploadPosterForm(forms.ModelForm):
    class Meta:
        model = models.Poster
        fields = ['name', 'movie', 'description', "image"]
