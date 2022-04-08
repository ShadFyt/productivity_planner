from urllib import response
from django.test import TestCase
from planner.models import Task


class HomePageTest(TestCase):
    def test_home_page_returns_correct_html(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "home.html")

    def test_can_save_POST_request(self):
        response = self.client.post("/", data={"task_text": "Write tests for homepage"})
        self.assertIn("Write tests for homepage", response.content.decode())
        self.assertTemplateUsed(response, "home.html")


class TaskModelTest(TestCase):
    def test_saving_and_retrieving_tasks(self):
        first_task = Task()
        first_task.text = "first task to do"
        first_task.save()

        second_task = Task()
        second_task.text = "2nd task to do"
        second_task.save()

        saved_tasks = Task.objects.all()
        self.assertEqual(saved_tasks.count(), 2)

        first_saved_task = saved_tasks[0]
        second_saved_task = saved_tasks[1]

        self.assertEqual(first_saved_task.text, "first task to do")
        self.assertEqual(second_saved_task.text, "2nd task to do")
