# api_project/api/views.py
# api/views.py (viewset example)
from rest_framework import generics
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

class BookListAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookList(generics.ListAPIView):
    """
    GET /api/books/  -> returns a JSON list of all books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
