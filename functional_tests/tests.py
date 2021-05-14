from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase
from selenium.common.exceptions import WebDriverException
import time
import unittest
MAX_WAIT=10

class NewVisitorTest(LiveServerTestCase):#(1)
    def setUp(self):#(3)
        self.brower = webdriver.Firefox()

    def tearDown(self):#(3)
        self.brower.quit()

    def check_for_row_in_list_table(self,row_text):
        table=self.brower.find_element_by_id('id_list_table')
        rows=table.find_elements_by_tag_name('tr')
        self.assertIn(row_text,[row.text for row in rows])

    def wait_for_row_in_list_table(self,row_text):
        start_time=time.time()
        while True:
            try:
                table=self.brower.find_element_by_id('id_list_table')
                rows=table.find_elements_by_tag_name('tr')
                self.assertIn(row_text,[row_text for row in rows])
                return
            except(AssertionError,WebDriverException)as e:
                if time.time()-start_time>MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def test_can_start_a_list_for_one_user(self):#(2)
        # Edith has heard about a cool new online to-do app.She goes
        # to check out its homepage
        self.brower.get(self.live_server_url)
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
       
        # when she hits enter, the page update ,and new the page lists
        # “1:Buy peacock feathers as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1:Buy peacock feathers')

        #there is still a text box inviting her to add another items.She
        #enter "Use peacock feathers to make a fly"(Edith is very methodical)
        inputbox=self.brower.find_element_by_id('id_new_item')
        inputbox.send_keys("Use peacock feathers to make a fly")
        inputbox.send_keys(Keys.ENTER)

        #the page updates again,and now shows both items on her list
        self.wait_for_row_in_list_table("1:Buy peacock feathers")
        self.wait_for_row_in_list_table("2:Use peacock feathers to make a fly")
        #Edith wonders whether the site will remaber her list.Then she sees
        #that the site has generated a unique URL for her -- there is some
        #explanatory text to that effect
        self.fail('Finish the test!')#(5)
        #Satisfied,she goes back to sleep
        
    def test_multiple_users_can_start_lists_at_different_urls(self):
        #Edith start a new to-do list
        self.brower.get(self.live_server_url)
        inputbox=self.brower.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1:Buy peacock feathers')

        #she notices that her list has a unique URL
        edith_list_url=self.brower.current_url
        self.assertRegex(edith_list_url,'/list/.+')
        #Now a new user,Francis,comes clong to the site

        ##We user a new brower session to make sure that no information
        ##of Edith's coming through from cookies etc
        self.brower.quit()
        self.brower=webdriver.Firefox()

        #Francis visits the home page.There is no sign of Edith's
        #list
        self.brower.get(self.live_server_url)
        page_text=self.brower.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers',page_text)
        self.assertNotIn('make a fly',page_text)

        #Francis starts a new list by entering a new list item.He
        #is less interesting than Edith...
        inputbox=self.brower.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1:Buy milk')

        #Francis gets his own unique URL
        francis_list_url=self.brower.current_url
        self.assertRegex(francis_list_url,'/list/.+')
        self.assertNotEqual(francis_list_url,edith_list_url)

        #Again,there is no trace of Edith's list
        page_text=self.brower.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers',page_text)
        self.assertIn('Buy milk',page_text)

        #satisfied,she goes back to sleep

if __name__=='__main__':#(6)
    unittest.main(warnings='ignore')#(7)