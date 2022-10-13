from django.db import models

# Create your models here.


class Movie(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to='images/')

    def __str__(self) -> str:
        return self.name
