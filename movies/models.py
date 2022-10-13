from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Movie(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


class Poster(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to='images/')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    uploader = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posters'
    )
    permitted_viewers = models.ManyToManyField(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"""
                name: {self.name} |
                movie: {self.movie} |
                uploader: {self.uploader}
        """
