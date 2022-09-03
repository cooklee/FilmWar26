from django.db import models


# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Category(models.Model):
    name = models.CharField(max_length=128)


class Movie(models.Model):
    title = models.CharField(max_length=128)
    year = models.IntegerField()
    category = models.ManyToManyField(Category)
    director = models.ForeignKey(Person, on_delete=models.CASCADE)
