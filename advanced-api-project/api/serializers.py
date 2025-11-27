from rest_framework import serializers
from .models import Author, Book
from datetime import datetime


# Book Serializer With Validation
class BookSerializer(serializers.ModelSerializer):

    # Custom rule: publication year cannot be in future
    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year can't be in the future.")
        return value

    class Meta:
        model = Book
        fields = '__all__'  # Serialize every field
        


# Author Serializer With Nested Books Display
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)  # Nested Relationship

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
