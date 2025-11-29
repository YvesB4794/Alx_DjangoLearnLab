# api/tests/test_views.py
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
from api.models import Author, Book
from rest_framework.authtoken.models import Token

User = get_user_model()

class BookAPITestCase(APITestCase):
    """
    Tests CRUD operations, filtering/searching/ordering, and permissions for Book endpoints.
    """

    def setUp(self):
        # Create authors
        self.author1 = Author.objects.create(name='Author One')
        self.author2 = Author.objects.create(name='Author Two')

        # Create some books
        self.book1 = Book.objects.create(title='Alpha', publication_year=2018, author=self.author1)
        self.book2 = Book.objects.create(title='Beta', publication_year=2020, author=self.author1)
        self.book3 = Book.objects.create(title='Gamma', publication_year=2021, author=self.author2)

        # Create a regular user and token
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.token = Token.objects.create(user=self.user)
        self.auth_header = {'HTTP_AUTHORIZATION': f'Token {self.token.key}'}

        # API endpoints
        self.list_url = reverse('api:book-list')           # e.g., /api/books/
        self.create_url = reverse('api:book-create')       # e.g., /api/books/create/

    def test_list_books_public(self):
        """Anyone can list books (GET)."""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # basic count check
        self.assertEqual(len(response.data), 3)

    def test_retrieve_book_detail(self):
        """Retrieve a single book detail."""
        url = reverse('api:book-detail', args=[self.book1.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Alpha')

    def test_create_book_requires_auth(self):
        """Unauthenticated users cannot create books."""
        payload = {'title': 'New Book', 'publication_year': 2022, 'author': self.author1.id}
        response = self.client.post(self.create_url, payload, format='json')
        # should be unauthorized or forbidden depending on config
        self.assertIn(response.status_code, (status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN))

    def test_create_book_with_auth(self):
        """Authenticated user can create a book."""
        payload = {'title': 'New Auth Book', 'publication_year': 2022, 'author': self.author1.id}
        response = self.client.post(self.create_url, payload, format='json', **self.auth_header)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Check DB
        self.assertTrue(Book.objects.filter(title='New Auth Book').exists())

    def test_update_book_with_auth(self):
        """Authenticated user can update a book."""
        url = reverse('api:book-update', args=[self.book1.pk])
        payload = {'title': 'Alpha Updated', 'publication_year': 2019, 'author': self.author1.id}
        response = self.client.put(url, payload, format='json', **self.auth_header)
        self.assertIn(response.status_code, (status.HTTP_200_OK, status.HTTP_202_ACCEPTED))
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Alpha Updated')

    def test_delete_book_with_auth(self):
        """Authenticated user can delete a book."""
        url = reverse('api:book-delete', args=[self.book2.pk])
        response = self.client.delete(url, **self.auth_header)
        self.assertIn(response.status_code, (status.HTTP_204_NO_CONTENT, status.HTTP_200_OK))
        self.assertFalse(Book.objects.filter(pk=self.book2.pk).exists())

    def test_filter_by_publication_year(self):
        """Filtering by publication_year works."""
        response = self.client.get(self.list_url, {'publication_year': 2020})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Only one book with 2020 in setUp
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['publication_year'], 2020)

    def test_search_by_title(self):
        """Search by title should find 'Alpha'."""
        response = self.client.get(self.list_url, {'search': 'Alpha'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        titles = [b['title'] for b in response.data]
        self.assertIn('Alpha', titles)

    def test_ordering_by_publication_year(self):
        """Ordering by publication_year returns sorted results."""
        response = self.client.get(self.list_url, {'ordering': 'publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [b['publication_year'] for b in response.data]
        self.assertEqual(years, sorted(years))

    def test_publication_year_validation(self):
        """Serializer should reject future publication_year."""
        future_year = 9999
        payload = {'title': 'Future', 'publication_year': future_year, 'author': self.author1.id}
        # Authenticated to test validation path
        response = self.client.post(self.create_url, payload, format='json', **self.auth_header)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('publication_year', response.data)
