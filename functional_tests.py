from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import unittest

from planner.models import Task


class NewVisitorTest(unittest.TestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element(By.ID, value="task_table")
        rows = table.find_elements(By.TAG_NAME, value="tr")
        self.assertIn(row_text, [row.text for row in rows])

    # Bob has heard about a new online productivity planner app.
    # He goes to check out the homepage
    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get("http://localhost:8000")

        # client notices the page title is 'Productivity Planner'
        self.assertIn("Productivity Planner", self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, value="h1").text
        self.assertIn("Productivity Planner For Software Developers", header_text)

        # client is invited to enter a new task
        inputbox = self.browser.find_element(By.ID, value="new_task")
        self.assertEqual(inputbox.get_attribute("placeholder"), "Enter a new task")
        # Client enters "Write tests for homepage"
        inputbox.send_keys("Write tests for homepage")
        # When the client hits enter, the page will update, and list
        # "Write tests for homepage"
        inputbox.send_keys(Keys.ENTER)
        # client enters a 2nd task to do
        inputbox = self.browser.find_element(By.ID, value="new_task")

        inputbox.send_keys("Write view logic for homepage")
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        self.check_for_row_in_list_table("Write tests for homepage")
        self.check_for_row_in_list_table("Write view logic for homepage")
        self.fail("Finished the test!")


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


if __name__ == "__main__":
    unittest.main()
