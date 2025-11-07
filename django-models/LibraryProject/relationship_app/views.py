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
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib import messages

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
    

# ✅ User Registration View
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Registration successful. You can now log in.")
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})


# ✅ User Login View
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome, {username}!")
                return redirect('list_books')
        messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})


# ✅ User Logout View
def logout_view(request):
    logout(request)
    return render(request, 'relationship_app/logout.html')




# ...existing code...