from rest_framework import serializers
from .models import Book, Name
from rest_framework.validators import ValidationError


class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'subtitle', 'author', 'isbn', 'price',)


class NameSerializers(serializers.ModelSerializer):
    class Meta:
        model = Name
        fields = ('id', 'name',)
