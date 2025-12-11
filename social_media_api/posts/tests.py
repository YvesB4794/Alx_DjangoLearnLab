from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from .models import Post, Comment
from rest_framework import status

User = get_user_model()

class PostCommentTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user('tester', password='pass')
        resp = self.client.post(reverse('token_obtain_pair'), {'username':'tester', 'password':'pass'}, format='json')
        # If token endpoint not wired yet, create token by login/register flow or use force_authenticate
        self.client.force_authenticate(user=self.user)

    def test_create_post(self):
        url = '/api/posts/'
        data = {'title':'t1','content':'c1'}
        resp = self.client.post(url, data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 1)

    def test_create_comment(self):
        post = Post.objects.create(author=self.user, title='t', content='c')
        url = '/api/comments/'
        data = {'post': post.id, 'content': 'nice'}
        resp = self.client.post(url, data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Comment.objects.count(), 1)
