from django.test import TestCase
from .models import BlogPost

class BlogPostTestCase(TestCase):
    def setUp(self):
        BlogPost.objects.create(title='Hello, world')

    def test_has_title(self):
        post = BlogPost.objects.get(title='Hello, world')

        title = post.get_title()

        self.assertTrue(title, 'Hello, world')
