from selenium import webdriver
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

        # He notices the page title is 'Productivity Planner'
        self.assertIn("Productivity Planner", self.browser.title)
        self.fail("Finished the test!")


if __name__ == "__main__":
    unittest.main()
