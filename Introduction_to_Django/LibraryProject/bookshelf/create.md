Open Django shell:
>>> from bookshelf.models import Book
>>> b = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
>>> b
# Expected output: <Book: 1984 by George Orwell>
>>> print(b)
# Expected output: 1984 by George Orwell
