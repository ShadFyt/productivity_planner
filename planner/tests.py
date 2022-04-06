from urllib import response
from django.test import TestCase


class HomePageTest(TestCase):
    def test_home_page_returns_correct_html(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "home.html")

    def test_can_save_POST_request(self):
        response = self.client.post("/", data={"task_text": "Write tests for homepage"})
        self.assertIn("Write tests for homepage", response.content.decode())
        self.assertTemplateUsed(response, "home.html")
