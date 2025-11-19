# api_project/api/urls.py
from django.urls import path
from .views import BookListAPIView
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = router.urls

urlpatterns = [
    path('books/', BookListAPIView.as_view(), name='api_books_list'),
]





