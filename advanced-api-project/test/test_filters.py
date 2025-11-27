from django.urls import reverse
from rest_framework.test import APITestCase
from api.models import Author, Book

class BookFilterSearchOrderingTests(APITestCase):
    def setUp(self):
        a = Author.objects.create(name='Author A')
        b = Author.objects.create(name='Author B')
        Book.objects.create(title='Alpha', publication_year=2018, author=a)
        Book.objects.create(title='Beta', publication_year=2020, author=a)
        Book.objects.create(title='Gamma', publication_year=2021, author=b)

    def test_filter_by_publication_year(self):
        url = reverse('api:book-list')
        resp = self.client.get(url, {'publication_year': 2020})
        assert resp.status_code == 200
        self.assertEqual(len(resp.data), 1)
        self.assertEqual(resp.data[0]['publication_year'], 2020)

    def test_search_by_title(self):
        url = reverse('api:book-list')
        resp = self.client.get(url, {'search': 'Alpha'})
        assert resp.status_code == 200
        self.assertEqual(len(resp.data), 1)
        self.assertEqual(resp.data[0]['title'], 'Alpha')

    def test_ordering(self):
        url = reverse('api:book-list')
        resp = self.client.get(url, {'ordering': 'publication_year'})
        years = [item['publication_year'] for item in resp.data]
        assert years == sorted(years)
