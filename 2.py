from selenium import webdriver
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
        self.fail('Finish the test!')#(5)
if __name__=='__main__':#(6)
    unittest.main(warnings='ignore')#(7)