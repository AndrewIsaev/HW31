from django.db import models


# Create your models here.
class Category(models.Model):
    name: str = models.CharField(max_length=200)


class Advertisement(models.Model):
    name: str = models.CharField(max_length=200)
    author: str = models.CharField(max_length=200)
    price: int = models.IntegerField()
    description: str = models.CharField(max_length=1000)
    address: str = models.CharField(max_length=1000)
    is_published: bool = models.BooleanField()
