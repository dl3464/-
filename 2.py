from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

import unittest
class NewVisitorTest(unittest.TestCase):#(1)
    def setUp(self):#(3)
        self.brower = webdriver.Firefox()
    def tearDown(self):#(3)
        self.brower.quit()
    def test_can_start_a_list_and_retrieve_it_later(self):#(2)
        # Edith has heard about a cool new online to-do app.She goes
        # to check out its homepage
        self.brower.get('http://localhost:8000')
        # she notices the page title and header mention to-do lists
        self.assertIn('To-Do',self.brower.title)#(4)
        header_text=self.brower.find_element_by_tag_name('h1').text
        self.assertIn('To-Do',header_text)
        # she is invited to enter a to-do item straight away
        inputbox=self.brower.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )
        # she types "buy peacock features" into a text box(Edith's hobby
        # is tying fly-finishing lures
        inputbox.send_keys('Buy peacock feathers')

        # when she hits enter, the page update ,and new the page lists
        # “1:Buy peacock feathers as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)
        times.sleep(1)

        table=self.brower.find_element_by_id('id_list_table')
        rows=table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text=='1:Buy peacock feathers' for row in rows),
            "New to-do item did not appear in table"
        )

        # there is still a text box inviting her to add another items.She
        # enter "Use peacock feathers to make a fly"(Edith is very methodical)
        self.fail('Finish the test!')#(5)
if __name__=='__main__':#(6)
    unittest.main(warnings='ignore')#(7)