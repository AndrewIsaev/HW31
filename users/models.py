from django.db import models


# Create your models here.
class User(models.Model):
    ROLE: list[tuple] = [
        ("admin", "админ"),
        ("moderator", "модератор"),
        ("member", "участник"),
    ]
    first_name: str = models.CharField(max_length=50)
    last_name: str = models.CharField(max_length=50)
    username: str = models.CharField(max_length=50)
    password: str = models.CharField(max_length=50)
    role: str = models.CharField(max_length=50, choices=ROLE, default="member")
    age: int = models.PositiveSmallIntegerField()
    locations: int = models.ManyToManyField("users.Location")


    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["username"]


class Location(models.Model):
    name: str = models.CharField(max_length=250)
    lat: float = models.DecimalField(max_digits=10, decimal_places=6, null=True)
    lng: float = models.DecimalField(max_digits=10, decimal_places=6, null=True)

    class Meta:
        verbose_name = "Локация"
        verbose_name_plural = "Локации"

    def __str__(self):
        return f"{self.name}"
