>>> from bookshelf.models import Book
>>> all_books = Book.objects.all()
>>> list(all_books)
# Expected output: [<Book: 1984 by George Orwell>]

>>> bk = Book.objects.get(title="1984")
>>> bk.title, bk.author, bk.publication_year
# Expected output: ('1984', 'George Orwell', 1949)
