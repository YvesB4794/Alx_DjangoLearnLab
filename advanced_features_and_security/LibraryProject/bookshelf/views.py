from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Bookshelf
from django.contrib.auth.decorators import login_required, permission_required
from .models import Book
from .forms import BookForm, BookSearchForm
from django.db.models import Q

@login_required
def list_books(request):
    books = Book.objects.filter(added_by=request.user)
    return render(request, 'bookshelf/list_books.html', {'books': books})

@login_required
def create_book(request):
    if request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")
        Book.objects.create(title=title, author=author, added_by=request.user)
        return redirect('bookshelf:list_books')
    return render(request, 'bookshelf/create_book.html')

@login_required
def my_bookshelves(request):
    shelves = Bookshelf.objects.filter(owner=request.user)
    return render(request, "bookshelf/my_shelves.html", {"shelves": shelves})

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    form = BookSearchForm(request.GET or None)
    books = Book.objects.none()
    if form.is_valid():
        q = form.cleaned_data.get('q')
        if q:
            # Use parameterized ORM queries; avoid .raw with string formatting
            books = Book.objects.filter(Q(title__icontains=q) | Q(author__icontains=q))
        else:
            books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books, 'search_form': form})

@permission_required('bookshelf.can_create', raise_exception=True)
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.added_by = request.user
            book.save()
            return redirect('bookshelf:book_list')
    else:
        form = BookForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})

@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    form = BookForm(request.POST or None, instance=book)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('bookshelf:book_list')
    return render(request, 'bookshelf/form_example.html', {'form': form})

@permission_required('bookshelf.can_delete', raise_exception=True)
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('bookshelf:book_list')
    return render(request, 'bookshelf/confirm_delete.html', {'book': book})