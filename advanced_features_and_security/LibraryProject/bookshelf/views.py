from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Book, Bookshelf
from django.contrib.auth.decorators import permission_required
from .models import Book


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