from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    added_by = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE,
    related_name="bookshelf_books_added"
    )

    def __str__(self):
        return self.title

class Bookshelf(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="bookshelves"
    )
    books = models.ManyToManyField(Book, related_name="shelves", blank=True)

    def __str__(self):
        return f"{self.name} ({self.owner.username})"
class CustomUser(AbstractUser):
    date_of_birth = None  # dummy placeholder
    profile_photo = None  # dummy placeholder    
