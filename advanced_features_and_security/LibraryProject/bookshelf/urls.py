from django.urls import path
from . import views

app_name = 'bookshelf'

urlpatterns = [
    path('', views.list_books, name='list_books'),
    path('add/', views.create_book, name='add_book'),
    path('shelves/', views.my_bookshelves, name='my_shelves'),
]
