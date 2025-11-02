>>> from bookshelf.models import Book
>>> bk = Book.objects.get(title="1984")
>>> bk.title = "Nineteen Eighty-Four"
>>> bk.save()
>>> Book.objects.get(pk=bk.pk).title
# Expected output: 'Nineteen Eighty-Four'
