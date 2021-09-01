from django.db.models.fields import SlugField
from django.test import TestCase
from blog.models import Post

class PostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Post.objects.create(title = "John Snow", slug = "theking")

    def test_title_label(self):
        post = Post.objects.get(id=1)
        title = post._meta.get_field('title').verbose_name
        self.assertEquals(title, 'title')

    def test_slug_label(self):
        post = Post.objects.get(id=1)
        SlugField = post._meta.get_field('slug').verbose_name
        self.assertEquals(SlugField, 'slug')

    def test_updated_on_label(self):
        post= Post.objects.get(id=1)
        updated_on = post._meta.get_field('updated_on').verbose_name
        self.assertEquals(updated_on, 'update on')

    def test_title_max_length(self):
        post = Post.objects.get(id=1)
        max_length = post._meta.get_field('title').max_length
        self.assertEquals(max_length, 200)
    
    def test_slug_max_length(self):
        post = Post.objects.get(id=1)
        max_length = post._meta.get_field('slug').max_length
        self.assertEquals(max_length, 200)

    def test_object_title(self):
        post = Post.objects.get(id=1)
        expected_object_name = f'{post.title}'
        self.assertEquals(expected_object_name, str(post))
