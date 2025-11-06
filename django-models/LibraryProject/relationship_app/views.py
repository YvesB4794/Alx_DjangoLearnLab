from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import DetailView
from .models import Book, Library


# ---------------------------
# Function-based View
# ---------------------------
def list_books(request):
    """Displays a list of all book titles and their authors."""
    books = Book.objects.all()
    # Render using the required template path
    return render(request, 'relationship_app/list_books.html', {'books': books})


# ---------------------------
# Class-based View
# ---------------------------
class LibraryDetailView(DetailView):
    """Displays details for a specific library, including all its books."""
    model = Library
    template_name = 'relationship_app/library_detail.html'  # make sure the path matches
    context_object_name = 'library'
