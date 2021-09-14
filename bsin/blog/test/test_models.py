from django.test import TestCase
from blog.models import Post
from django.contrib.auth.models import User

class PostTestCase(TestCase):

    def setUp(self):
        User.objects.create(username="admin")

        Post.objects.create(
            title="Testando",
            author=User.objects.get(username="admin")
        )

    def test_retorno_str(self):
        p1 = Post.objects.get(title='Testando')
        self.assertEquals(p1.__str__(), 'Testando')

