from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException

import time

MAX_WAIT = 10


class NewVisitorTest(LiveServerTestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:
        self.browser.quit()

    def wait_for_row_in_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element(By.ID, value="task_table")
                rows = table.find_elements(By.TAG_NAME, value="tr")
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

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
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_table("Write tests for homepage")

        # client enters a 2nd task to do
        inputbox1 = self.browser.find_element(By.ID, value="new_task")

        inputbox1.send_keys("Write view logic for homepage")
        inputbox1.send_keys(Keys.ENTER)

        self.wait_for_row_in_table("Write tests for homepage")
        self.wait_for_row_in_table("Write view logic for homepage")
        self.fail("Finished the test!")
