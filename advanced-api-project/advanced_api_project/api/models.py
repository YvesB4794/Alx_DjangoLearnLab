from django.db import models
from datetime import date

"""
Author Model:
Represents a writer in the system.
Only contains the author's name, but relates to multiple books.
"""

class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


"""
Book Model:
Represents a book written by an author.
Linked to Author using a ForeignKey (one-to-many relationship).
"""

class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
