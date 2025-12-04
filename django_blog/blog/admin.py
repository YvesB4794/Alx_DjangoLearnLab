from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'published_date')
    list_filter = ('published_date', 'author')
    search_fields = ('title', 'content', 'author__username')
