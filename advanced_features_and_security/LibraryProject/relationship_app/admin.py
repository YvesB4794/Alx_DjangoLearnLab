# relationship_app/admin.py
from django.contrib import admin
from .models import Author, Book, Library, Librarian
from .models import UserProfile

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Library)
admin.site.register(Librarian)

# LibraryProject/relationship_app/admin.py

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')
    list_select_related = ('user',)
