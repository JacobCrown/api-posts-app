from django.test import TestCase
from django.contrib.auth.models import User

from .models import Post


class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        testuser1 = User.objects.create_user(
            username='user1', password='testpass123'
        )
        testuser1.save()

        test_post = Post.objects.create(
            author=testuser1, title='First Post', body='Body content ...'
        )
        test_post.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        author = f'{post.author}'
        title = f'{post.title}'
        body = f'{post.body}'
        self.assertEqual(author, 'user1')
        self.assertEqual(title, 'First Post')
        self.assertEqual(body, 'Body content ...')