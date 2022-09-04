from django.core.exceptions import ValidationError
from django.db import models


# Create your models here.
from django.urls import reverse


class Person(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    year = models.IntegerField(default=1970)
    #movie_set
    #movie_set

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Studio(models.Model):
    name = models.CharField(max_length=128)
    city = models.CharField(max_length=50)
    year = models.IntegerField()
    ceo = models.ForeignKey(Person, on_delete=models.CASCADE)


class Category(models.Model):
    name = models.CharField(max_length=128)

    def get_absolute_url(self):
        return reverse('update_category', args=(self.id, ))

    def __str__(self):
        return f"{self.name}"

def year_validation(value):
    if value < 1908:
        raise ValidationError("Rok nie moze byc przed 1908")

class Movie(models.Model):
    title = models.CharField(max_length=128)
    year = models.IntegerField(validators=[year_validation])
    category = models.ManyToManyField(Category)
    director = models.ForeignKey(Person, on_delete=models.CASCADE)


    def get_absolute_url(self):
        return reverse("update_movie", args=(self.id,))

    def __str__(self):
        return f"{self.title}"