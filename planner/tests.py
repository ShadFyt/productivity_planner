from urllib import response
from django.test import TestCase
from planner.models import Task


class HomePageTest(TestCase):
    def test_home_page_returns_correct_html(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")

    def test_only_save_tasks_when_necessary(self):
        self.client.get("/")
        self.assertEqual(Task.objects.count(), 0)

    def test_can_save_POST_request(self):
        response = self.client.post("/", data={"task_text": "Write tests for homepage"})

        self.assertEqual(Task.objects.count(), 1)
        new_task = Task.objects.first()
        self.assertEqual(new_task.text, "Write tests for homepage")

    def test_redirects_after_POST(self):
        response = self.client.post("/", data={"task_text": "Write tests for homepage"})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response["location"], "/")

    def test_display_all_task(self):
        Task.objects.create(text="task 1")
        Task.objects.create(text="task 2")

        response = self.client.get("/")
        self.assertIn("task 1", response.content.decode())
        self.assertIn("task 2", response.content.decode())


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
