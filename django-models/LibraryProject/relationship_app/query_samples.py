import os
import django

# configure Django settings and setup
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def create_sample_data():
    # create author and books
    author, _ = Author.objects.get_or_create(name='George Orwell')
    b1, _ = Book.objects.get_or_create(title='1984', author=author)
    b2, _ = Book.objects.get_or_create(title='Animal Farm', author=author)

    # create library and add books
    lib, _ = Library.objects.get_or_create(name='Central Library')
    lib.books.add(b1, b2)

    # create librarian for the library
    Librarian.objects.get_or_create(name='Alice Smith', library=lib)

    return author, lib

def query_books_by_author(author_name):
    author = Author.objects.filter(name=author_name).first()
    if not author:
        print(f"No author named {author_name}")
        return []
    books = list(author.books.all())
    print(f"Books by {author_name}: {[b.title for b in books]}")
    return books

def list_books_in_library(library_name):
    lib = Library.objects.filter(name=library_name).first()
    if not lib:
        print(f"No library named {library_name}")
        return []
    books = list(lib.books.all())
    print(f"Books in {library_name}: {[b.title for b in books]}")
    return books

def get_librarian_for_library(library_name):
    lib = Library.objects.filter(name=library_name).first()
    if not lib:
        print(f"No library named {library_name}")
        return None
    # Because of one-to-one, access via related attribute
    librarian = getattr(lib, 'librarian', None)
    print(f"Librarian for {library_name}: {librarian.name if librarian else 'None'}")
    return librarian

if __name__ == '__main__':
    author, lib = create_sample_data()
    query_books_by_author('George Orwell')
    list_books_in_library('Central Library')
    get_librarian_for_library('Central Library')
