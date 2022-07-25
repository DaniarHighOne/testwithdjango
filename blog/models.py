from statistics import mode
from turtle import title
from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.title