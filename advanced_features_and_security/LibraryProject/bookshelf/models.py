from django.db import models
from django.conf import settings


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)

    # Link each book to a user from the CustomUser model
    added_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="books_added"
    )

    def __str__(self):
        return self.title


class Bookshelf(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="bookshelves"
    )
    name = models.CharField(max_length=255)
    books = models.ManyToManyField(Book, related_name="bookshelves")

    def __str__(self):
        return f"{self.name} ({self.owner.username})"
