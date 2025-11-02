>>> from bookshelf.models import Book
>>> bk = Book.objects.get(title="Nineteen Eighty-Four")
>>> bk.delete()
# Expected output: (1, {'bookshelf.Book': 1})

>>> list(Book.objects.all())
# Expected output: []
