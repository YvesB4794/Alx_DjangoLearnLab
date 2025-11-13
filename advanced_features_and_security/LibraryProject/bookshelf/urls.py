from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('books/add/', views.create_book, name='add_book'),
    path('shelves/', views.my_bookshelves, name='my_shelves'),
]
