from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def get_books_by_author(author):
    books = Book.objects.filter(author=author)
    return books

# List all books in a specific library
def get_books_in_library(library):
    books = library.books.all()
    return books

# Retrieve the librarian for a specific library
def get_librarian_for_library(library):
    librarian = Librarian.objects.get(library=library)
    return librarian
