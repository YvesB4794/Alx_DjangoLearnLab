from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import DetailView
from .models import Book, Library


# ---------------------------
# Function-based View
# ---------------------------
def list_books(request):
    """Displays a simple text list of all book titles and their authors."""
    books = Book.objects.all()
    # Simple text response (for automated checks)
    response_text = "\n".join([f"{book.title} by {book.author.name}" for book in books])
    return HttpResponse(response_text)


# ---------------------------
# Class-based View
# ---------------------------
class LibraryDetailView(DetailView):
    """Displays details for a specific library, including all its books."""
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'
