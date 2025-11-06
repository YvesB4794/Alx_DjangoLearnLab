# relationship_app/query_samples.py
# Script to create sample data and run example queries for relationships
# This file is intended to be executed inside the Django project using:
# python manage.py shell -c "exec(open('relationship_app/query_samples.py').read())"

from relationship_app.models import Author, Book, Library, Librarian
from django.db import transaction

def create_sample_data():
    # Use transaction.atomic so the sample creation is atomic
    with transaction.atomic():
        # Clear existing sample data (optional, helpful during repeated runs)
        Librarian.objects.all().delete()
        Library.objects.all().delete()
        Book.objects.all().delete()
        Author.objects.all().delete()

        # Create Authors
        orwell = Author.objects.create(name="George Orwell")
        tolkien = Author.objects.create(name="J.R.R. Tolkien")

        # Create Books
        b1 = Book.objects.create(title="1984", author=orwell)
        b2 = Book.objects.create(title="Animal Farm", author=orwell)
        b3 = Book.objects.create(title="The Hobbit", author=tolkien)
        b4 = Book.objects.create(title="The Lord of the Rings", author=tolkien)

        # Create Libraries
        lib1 = Library.objects.create(name="Central Library")
        lib2 = Library.objects.create(name="Community Library")

        # Add books to libraries (ManyToMany)
        lib1.books.add(b1, b3, b4)
        lib2.books.add(b2, b3)

        # Create librarians (OneToOne)
        Librarian.objects.create(name="Alice M.", library=lib1)
        Librarian.objects.create(name="Bob K.", library=lib2)

        print("Sample data created.")
        return {
            'orwell': orwell,
            'tolkien': tolkien,
            'books': [b1, b2, b3, b4],
            'libraries': [lib1, lib2]
        }

def query_books_by_author(author_name):
    print(f"\n=== Books by author: {author_name} ===")
    try:
        author = Author.objects.get(name=author_name)
        books = author.books.all()
        for b in books:
            print(f"- {b.title}")
        if not books:
            print("No books found for that author.")
    except Author.DoesNotExist:
        print("Author not found.")

def list_books_in_library(library_name):
    print(f"\n=== Books in library: {library_name} ===")
    try:
        lib = Library.objects.get(name=library_name)
        for b in lib.books.all():
            print(f"- {b.title} (author: {b.author.name})")
    except Library.DoesNotExist:
        print("Library not found.")

def get_librarian_for_library(library_name):
    print(f"\n=== Librarian for library: {library_name} ===")
    try:
        lib = Library.objects.get(name=library_name)
        # OneToOne relation: access librarian via related name 'librarian'
        print(lib.librarian)  # __str__ will show name and library
    except Library.DoesNotExist:
        print("Library not found.")
    except Librarian.DoesNotExist:
        print("No librarian assigned to this library.")

if __name__ == "__main__":
    # Create data and run sample queries
    print("Running relationship samples...")
    create_sample_data()
    query_books_by_author("George Orwell")
    list_books_in_library("Central Library")
    get_librarian_for_library("Central Library")
