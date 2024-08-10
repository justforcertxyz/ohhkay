from django.test import TestCase, Client
from unittest import skip
from .models import Blog
from django.urls import reverse


class BlogModelTest(TestCase):
    def test_Blog_model_exists(self):
        blog_count = Blog.objects.count()

        self.assertEqual(blog_count, 0)
    
    def test___str__(self):
        title = "Test Blog"
        slug = "test_blog"
        blog = Blog.objects.create(title=title, slug=slug)

        self.assertEqual(str(blog), blog.title)

class IndexPageTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.index_url = reverse('blog:index')

    def test_index_page_returns_correct_response(self):
        response = self.client.get(self.index_url)
        self.assertTemplateUsed(response, 'blog/index.html')
        self.assertTemplateUsed(response, 'landing/base.html')
        self.assertEqual(response.status_code, 200)
    
    def test_index_page_returns_corrent_content(self):
        response = self.client.get(self.index_url)
        self.assertContains(response, "<title>Blog")


class DetailPageTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.blog = Blog.objects.create(title="Some Blog", slug="some_slug")
        self.detail_url = reverse('blog:detail', kwargs={'slug': self.blog.slug})

    def test_index_page_returns_correct_response(self):
        response = self.client.get(self.detail_url)
        self.assertTemplateUsed(response, 'blog/detail.html')
        self.assertTemplateUsed(response, 'landing/base.html')
        self.assertEqual(response.status_code, 200)
    
    def test_index_page_returns_corrent_content(self):
        response = self.client.get(self.detail_url)
        self.assertContains(response, f"<title>{self.blog.title}")