from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MinValueValidator, MaxValueValidator

'''''
class Author(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(20)
    def __str__(self):
        return self.name
    '''''

class Author(models.Model):
    name = models.CharField(max_length=200)
    age = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        validators=[MinValueValidator(0), MaxValueValidator(120)],
        help_text="Author age in years (optional, 0-120)"
    )
    def __str__(self):
        return self.name    



class Library(models.Model):
    name = models.CharField(max_length=200)
    '''''
    books = models.ManyToManyField(Book, related_name='libraries', blank=True)
    '''
    location = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=300)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    library = models.ForeignKey(Library, on_delete=models.CASCADE)
    published_date = models.DateField()


    def __str__(self):
        return self.title

class Librarian(models.Model):
    name = models.CharField(max_length=200)
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name='librarian')

    def __str__(self):
        return f"{self.name} ({self.library.name})"
# ...existing code...

class UserProfile(models.Model):
    ROLE_ADMIN = 'Admin'
    ROLE_LIBRARIAN = 'Librarian'
    ROLE_MEMBER = 'Member'
    ROLE_CHOICES = [
        (ROLE_ADMIN, 'Admin'),
        (ROLE_LIBRARIAN, 'Librarian'),
        (ROLE_MEMBER, 'Member'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=ROLE_MEMBER)

    def __str__(self):
        return f"{self.user.username} ({self.role})"


# Signal to create/update UserProfile automatically
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    else:
        # ensure profile exists in case user was created in another way
        UserProfile.objects.get_or_create(user=instance)

        # LibraryProject/relationship_app/models.py

class Meta:
        permissions = [
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book"),
        ]
