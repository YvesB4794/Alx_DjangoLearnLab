# api/views.py
"""
Generic and custom views for the Book model.

We use DRF's generic views:
- ListAPIView: list all objects (GET)
- RetrieveAPIView: get a single object (GET)
- CreateAPIView: create new object (POST)
- UpdateAPIView: update existing object (PUT/PATCH)
- DestroyAPIView: delete object (DELETE)

Permissions: Read views are public; write views require authentication.
"""

from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Book
from .serializers import BookSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from .permissions import IsAdminOrReadOnly

# List all books (GET /api/books/)
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'author__name']
    ordering_fields = ['publication_year', 'title']
    # Read is allowed for unauthenticated users (default), but global settings may apply


# Retrieve single book (GET /api/books/<pk>/)
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Create a new book (POST /api/books/create/)

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        # Example: log or attach additional data before saving
        serializer.save()


# Update existing book (PUT/PATCH /api/books/<pk>/update/)
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # require auth to update

# Delete a book (DELETE /api/books/<pk>/delete/)
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
#    permission_classes = [IsAuthenticatedOrReadOnly]  # require auth to delete
    permission_classes = [IsAdminOrReadOnly]   # only admin can delete
