from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone


class Genre(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20, null=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='articles/', null=True)
    genre = models.ManyToManyField(Genre)
    title = models.CharField(max_length=200)
    text = models.TextField()
    slug = models.SlugField(max_length=25, default='')
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("title", kwargs={"slug": self.genre.first().slug, "title_slug": self.slug})


class PostDescription(models.Model):
    image = models.ImageField(upload_to='articles/', null=True)
    text = models.TextField(null=True)
    author = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True)


class Vote(models.Model):
    value = models.SmallIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Post, on_delete=models.CASCADE)
    voted_on = models.DateTimeField(auto_now=True)
