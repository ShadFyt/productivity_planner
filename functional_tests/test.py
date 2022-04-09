from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


class NewVisitorTest(LiveServerTestCase):
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
        self.browser.get(self.live_server_url)

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
        inputbox.send_keys(Keys.RETURN)
        time.sleep(1)
        # client enters a 2nd task to do
        inputbox1 = self.browser.find_element(By.ID, value="new_task")

        inputbox1.send_keys("Write view logic for homepage")
        inputbox1.send_keys(Keys.ENTER)
        time.sleep(5)

        self.check_for_row_in_list_table("Write tests for homepage")
        self.check_for_row_in_list_table("Write view logic for homepage")
        self.fail("Finished the test!")
