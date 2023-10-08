
from django.core import exceptions
from django.db import models


def separator_validator(value):
    if ', ' not in value:
        raise exceptions.ValidationError("The values should be separated by ', '!")
    return value


class Recipe(models.Model):
    title = models.CharField(
        max_length=30,
    )

    image_url = models.URLField()

    description = models.TextField()

    ingredients = models.CharField(
        max_length=250,
        validators=[separator_validator],
    )

    time = models.IntegerField()
