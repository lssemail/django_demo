from django.db import models

# Create your models here.


class Book(models.Model):
    id = models.Index
    author = models.CharField(max_length=32)
    description = models.CharField(max_length=100)
    isbn = models.CharField(max_length=100)
    reader = models.CharField(max_length=32)
    title = models.CharField(max_length=100)
    price = models.FloatField()
    stock = models.IntegerField()
    sales = models.IntegerField()
