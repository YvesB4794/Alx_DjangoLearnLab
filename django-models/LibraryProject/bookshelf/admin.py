# ...existing code...
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('author', 'publication_year')
    search_fields = ('title', 'author')
    ordering = ('title',)
    list_per_page = 25

admin.site.register(Book, BookAdmin)
# ...existing code...