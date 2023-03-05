from django.db import models
from django.core.validators import MinLengthValidator

from ads.validtors import check_is_published
from users.models import User


# Create your models here.
class Category(models.Model):
    name: models.CharField = models.CharField(max_length=200)
    slug = models.SlugField(max_length=10, validators=[MinLengthValidator(5)])

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Advertisement(models.Model):
    name: models.CharField = models.CharField(max_length=200, null=False, validators=[MinLengthValidator(10)])
    author: models.ForeignKey = models.ForeignKey(User, on_delete=models.CASCADE)
    price: models.PositiveIntegerField = models.PositiveIntegerField()
    description: models.CharField = models.CharField(max_length=1000, null=True)
    is_published: models.BooleanField = models.BooleanField(validators=[check_is_published])
    image: models.ImageField = models.ImageField(upload_to="images/")
    category: models.ForeignKey = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"

    def __str__(self):
        return self.name


class Selection(models.Model):
    name = models.CharField(max_length=50)
    items = models.ManyToManyField(Advertisement)
    owner = models.ForeignKey("users.User", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Подборка"
        verbose_name_plural = "Подборки"

    def __str__(self):
        return self.name
