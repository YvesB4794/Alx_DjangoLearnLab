# api_project/api/urls.py
from django.urls import path, include
from .views import BookListAPIView
from rest_framework.routers import DefaultRouter
from .views import BookViewSet
from .views import BookList

router = DefaultRouter()
# Register the viewset for full CRUD under 'books_all'
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = router.urls

urlpatterns = [
    path('books/', BookListAPIView.as_view(), name='api_books_list'),
    path('books/', BookList.as_view(), name='book-list'),
     # include router URLs for the viewset (full CRUD)
    path('', include(router.urls)),
]

