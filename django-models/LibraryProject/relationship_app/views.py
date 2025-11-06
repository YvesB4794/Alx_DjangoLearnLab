from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView   # ✅ exact import required
from .models import Book, Library   # ✅ includes Library import

# ---------------------------
# Function-based View
# ---------------------------
def list_books(request):
    """Displays a list of all book titles and their authors."""
    books = Book.objects.all()
    # ✅ make sure template path matches
    return render(request, 'relationship_app/list_books.html', {'books': books})


# ---------------------------
# Class-based View
# ---------------------------
class LibraryDetailView(DetailView):
    """Displays details for a specific library, including all its books."""
    model = Library
    template_name = 'relationship_app/library_detail.html'  # ✅ correct template path
    context_object_name = 'library'
