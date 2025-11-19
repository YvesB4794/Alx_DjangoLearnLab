# api_project/api/views.py
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from .models import Book
from .serializers import BookSerializer


class BookListAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookList(generics.ListAPIView):
    """
    GET /api/books/  -> returns a JSON list of all books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    """
    CRUD for Book.
    - Read (GET) allowed to everyone (because settings use IsAuthenticatedOrReadOnly).
    - Create/Update/Delete require authentication (Token or Session).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Example: require admin role for deletes (optional)
    def get_permissions(self):
        # Allow only admins to DELETE
        if self.action == 'destroy':
            return [IsAdminUser()]
        return super().get_permissions()
