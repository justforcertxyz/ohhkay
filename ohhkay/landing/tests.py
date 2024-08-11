from django.test import TestCase, Client
from unittest import skip
from django.urls import reverse


class IndexPageTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.index_url = reverse('landing:index')

    def test_index_page_returns_correct_response(self):
        response = self.client.get(self.index_url)
        self.assertTemplateUsed(response, 'landing/index.html')
        self.assertTemplateUsed(response, 'landing/base.html')
        self.assertEqual(response.status_code, 200)

    def test_index_page_returns_corrent_content(self):
        response = self.client.get(self.index_url)
        self.assertContains(response, "<title>Home")


class LinksPageTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.links_url = reverse('landing:links')

    def test_links_page_returns_correct_response(self):
        response = self.client.get(self.links_url)
        self.assertTemplateUsed(response, 'landing/links.html')
        self.assertTemplateUsed(response, 'landing/base.html')
        self.assertEqual(response.status_code, 200)

    def test_links_page_returns_corrent_content(self):
        response = self.client.get(self.links_url)
        self.assertContains(response, "<title>Links")


class RecommendationsPageTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.recommendations_url = reverse('landing:recommendations')

    def test_recommendations_page_returns_correct_response(self):
        response = self.client.get(self.recommendations_url)
        self.assertTemplateUsed(response, 'landing/recommendations.html')
        self.assertTemplateUsed(response, 'landing/base.html')
        self.assertEqual(response.status_code, 200)

    def test_recommendations_page_returns_corrent_content(self):
        response = self.client.get(self.recommendations_url)
        self.assertContains(response, "<title>Recommendations")
