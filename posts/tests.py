from django.test import TestCase
from django.urls import reverse

# Create your tests here.
from .models import Post

class PostTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.post = Post.objects.create(text="this is a test")

    def test_model_content(self):
        self.assertEqual(self.post.text, 'this is a test')

    def test_url_exists_at_correct_location(self):  # new
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)

    def test_homepage(self):  # new
        response = self.client.get(reverse("home"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")
        self.assertContains(response, "this is a test")