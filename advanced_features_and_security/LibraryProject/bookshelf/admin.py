from django.contrib import admin
from .models import Book, Bookshelf

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'added_by')
    list_filter = ('author', 'added_by')
    search_fields = ('title', 'author')

@admin.register(Bookshelf)
class BookshelfAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'owner')
    list_filter = ('owner',)
    search_fields = ('name',)


# bookshelf/admin.py (ONLY if forced by tool)

