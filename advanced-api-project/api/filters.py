# api/filters.py
import django_filters
from .models import Book

class BookFilter(django_filters.FilterSet):
    # Example: allow filtering publication_year__gte and publication_year__lte
    publication_year__gte = django_filters.NumberFilter(field_name='publication_year', lookup_expr='gte')
    publication_year__lte = django_filters.NumberFilter(field_name='publication_year', lookup_expr='lte')

    class Meta:
        model = Book
        fields = {
            'publication_year': ['exact', 'gte', 'lte'],
            'author': ['exact'],
            'title': ['icontains'],
        }
