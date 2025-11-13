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
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout  # ✅ add this line
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
'''
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib import messages
'''

from django.contrib.auth.decorators import user_passes_test, login_required
from django.http import HttpResponse

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book, Author, Library
from django import forms



# LibraryProject/relationship_app/views.py



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


# Function to register a new user
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # ✅ Uses login from django.contrib.auth
            messages.success(request, 'Registration successful.')
            return redirect('list_books')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})


# Function to handle login
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)  # ✅ Uses login from django.contrib.auth
                messages.success(request, f'Welcome back, {username}!')
                return redirect('list_books')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})


# Function to handle logout
def logout_view(request):
    logout(request)  # ✅ Uses logout from django.contrib.auth
    messages.info(request, 'You have been logged out successfully.')
    return render(request, 'relationship_app/logout.html')

# Make sure you have these imports (Book/Library may already exist)
from .models import UserProfile

# Helper role-check functions
def is_admin(user):
    try:
        return user.is_authenticated and user.profile.role == UserProfile.ROLE_ADMIN
    except Exception:
        return False

def is_librarian(user):
    try:
        return user.is_authenticated and user.profile.role == UserProfile.ROLE_LIBRARIAN
    except Exception:
        return False

def is_member(user):
    try:
        return user.is_authenticated and user.profile.role == UserProfile.ROLE_MEMBER
    except Exception:
        return False

# Admin view
@user_passes_test(is_admin, login_url='/login/')
def admin_view(request):
    # render a template for admin
    return render(request, 'relationship_app/admin_view.html')

# Librarian view
@user_passes_test(is_librarian, login_url='/login/')
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

# Member view
@user_passes_test(is_member, login_url='/login/')
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

from django.core.exceptions import PermissionDenied
...
@user_passes_test(is_admin)
def admin_view(request):
    if not is_admin(request.user):
        raise PermissionDenied
    ...


# LibraryProject/relationship_app/views.py


# Simple form for adding/editing books
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'library', 'published_date']


# View to add a new book (requires "can_add_book")
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm()
    return render(request, 'relationship_app/add_book.html', {'form': form})


# View to edit a book (requires "can_change_book")
@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/edit_book.html', {'form': form, 'book': book})


# View to delete a book (requires "can_delete_book")
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('list_books')
    return render(request, 'relationship_app/delete_book.html', {'book': book})

