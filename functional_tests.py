from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:
        self.browser.quit()

    # Bob has heard about a new online productivity planner app.
    # He goes to check out the homepage
    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get("http://localhost:8000")

        # client notices the page title is 'Productivity Planner'
        self.assertIn("Productivity Planner", self.browser.title)
        header_text = self.browser.find_element_by_tag_name("h1").text
        self.assertIn("Productivity Planner For Software Developers ", header_text)

        # client is invited to enter a new task
        inputbox = self.browser.find_element_by_id("new_task")
        self.assertEqual(inputbox.get_attribute("placeholder"), "Enter a new task")
        # Client enters "Write tests for homepage"
        inputbox.send_keys("Write tests for homepage")
        # When the client hits enter, the page will update, and list
        # "Write tests for homepage"
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        table = self.browser.find_element_by_id("task_table")
        rows = table.find_element_by_tag_name("tr")
        self.assertTrue(any(row.text == "Write tests for homepage" for row in rows))
        self.fail("Finished the test!")


if __name__ == "__main__":
    unittest.main()
