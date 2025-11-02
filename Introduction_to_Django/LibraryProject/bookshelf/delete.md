>>> from bookshelf.models import Book
>>> book = Book.objects.get(title="Nineteen Eighty-Four")
>>> result = book.delete()
>>> result
# Expected output: (1, {'bookshelf.Book': 1})
>>> list(Book.objects.all())
# Expected output: []