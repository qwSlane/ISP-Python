from django.db import models


class Client(models.Model):
    nickname = models.CharField(max_length=25)
    rating = models.FloatField()


class Item(models.Model):
    name = models.CharField(max_length=40)
    brand = models.CharField(max_length=20)
    release_date = models.DateField()
    retail_price = models.FloatField()
    goat_price = models.FloatField()
    description = models.TextField()


class Title(models.Model):
    content = models.TextField
    date = models.DateField()


class Photo(models.Model):
    url = models.CharField(max_length=100)
    parent_item = models.ForeignKey(Item, related_name='images', on_delete=models.CASCADE)
    parent_title = models.ForeignKey(Title, related_name='images', on_delete=models.CASCADE)


