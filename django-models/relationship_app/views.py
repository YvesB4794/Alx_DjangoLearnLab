from django.shortcuts import render
from .models import Author, Book, Library, Librarian

def author_books(request, author_name):
    books = Book.objects.filter(author__name=author_name)
    return render(request, 'relationship_app/author_books.html', {'books': books})

def library_books(request, library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    return render(request, 'relationship_app/library_books.html', {'books': books})

def librarian_info(request, library_name):
    librarian = Librarian.objects.get(library__name=library_name)
    return render(request, 'relationship_app/librarian_info.html', {'librarian': librarian})