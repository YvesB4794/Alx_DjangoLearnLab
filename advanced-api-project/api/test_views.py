from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from api.models import Book, Author

class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create test user for authentication
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword123"
        )

        # Login user for authenticated requests
        self.client = APIClient()
        self.client.login(username="testuser", password="testpassword123")   # <--- REQUIRED

        # Test separate DB (Django automatically isolates test database)
        self.author = Author.objects.create(name="Author Test")
        self.book1 = Book.objects.create(title="Book One", publication_year=2020, author=self.author)
        self.book2 = Book.objects.create(title="Book Two", publication_year=2023, author=self.author)

        self.list_url = reverse("book-list")
        self.detail_url = reverse("book-detail", kwargs={"pk": self.book1.id})

        
def test_unauthenticated_access_fails(self):
    self.client.logout()
    response = self.client.get(self.list_url)
    self.assertIn(response.status_code, [401, 403])  # depending on permissions config

    # ------------------ CRUD TESTS ------------------

    def test_create_book(self):
        """Should create a new Book entry"""
        data = {
            "title": "New Book",
            "publication_year": 2024,
            "author": self.author.id
        }
        response = self.client.post(self.list_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_book_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 2)

    def test_update_book(self):
        update_data = {"title": "Updated Title", "publication_year": 2020, "author": self.author.id}
        response = self.client.put(self.detail_url, update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Title")

    def test_delete_book(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    # ------------------ FILTER / SEARCH / ORDER ------------------

    def test_filter_books_by_year(self):
        response = self.client.get(f"{self.list_url}?publication_year=2023")
        self.assertEqual(len(response.data), 1)

    def test_search_books(self):
        response = self.client.get(f"{self.list_url}?search=Python")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Python Basics", str(response.data))

    def test_order_books(self):
        response = self.client.get(f"{self.list_url}?ordering=-publication_year")
        self.assertEqual(response.data[0]['publication_year'], 2023)
