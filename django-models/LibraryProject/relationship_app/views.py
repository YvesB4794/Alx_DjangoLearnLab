'''from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Book, Library   # ✅ includes "from .models import Library"

# ---------------------------
# Function-based View
# ---------------------------
def list_books(request):
    """Displays a list of all book titles and their authors."""
    books = Book.objects.all()
    # ✅ required explicit template path
    return render(request, 'relationship_app/list_books.html', {'books': books})


# ---------------------------
# Class-based View
# ---------------------------
class LibraryDetailView(DetailView):
    """Displays details for a specific library, including all its books."""
    model = Library
    template_name = 'relationship_app/library_detail.html'  # ✅ correct template path
    context_object_name = 'library'.    
    '''




''''
# thisis the corrected code 2
from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView  # ✅ exact import required
from .models import Book, Library  # ✅ must import both models


# ---------------------------
# Function-based View
# ---------------------------
def list_books(request):
    """Displays a list of all book titles and their authors."""
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


# ---------------------------
# Class-based View
# ---------------------------
class LibraryDetailView(DetailView):
    """Displays details for a specific library, including all its books."""
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
'''
    # this method is optional since DetailView handles it, but included for clarity. Final

# ...existing code...
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Book, Library

def list_books(request):
    """
    Function-based view that renders a simple list of book titles and their authors.
    URL: /books/
    """
    books = Book.objects.select_related('author').all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    """
    Class-based DetailView that shows a library and lists all books in it.
    URL: /library/<pk>/
    """
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        # safe access to related objects
        ctx['books'] = self.object.books.select_related('author').all()
        try:
            ctx['librarian'] = self.object.librarian
        except Exception:
            ctx['librarian'] = None
        return ctx
# ...existing code...