from rest_framework import serializers
from datetime import date
from .models import Author, Book


"""
BookSerializer:
Serializes all fields from the Book model.
Includes custom validation to ensure publication_year is not in the future.
"""

class BookSerializer(serializers.ModelSerializer):

    # Custom validation
    def validate_publication_year(self, value):
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']


"""
AuthorSerializer:
Serializes author data.
Includes a nested BookSerializer to display all books by an author.
"""

class AuthorSerializer(serializers.ModelSerializer):
    # Nest related books
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
