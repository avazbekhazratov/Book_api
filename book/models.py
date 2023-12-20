from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    content = models.TextField()
    isbn = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.title


class Name(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
