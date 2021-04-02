from selenium import webdriver

brower=webdriver.Firefox()

#Edith has heard about a cool new online to-do app.She goes
#to check out its homepage
brower.get('http://localhost:8000')

#she notices the page title and header mention to-do lists
assert 'To-Do' in brower.title

#she is invited to enter a to-do item straight away

#she types "buy peacock features" into a text box(Edith's hobby
#is tying fly-finishing lures

#when she hits enter, the page update ,and new the page lists
#“1:Buy peacock feathers as an item in a to-do list

#there is still a text box inviting her to add another items.She
#enter "Use peacock feathers to make a fly"(Edith is very methodical)

#the page updates again,and now shows both items on her list

#Edith wonders whether the site will remaber her list.Then she sees
#that the site has generated a unique URL for her -- there is some
#explanatory text to that effect

#she visits that URL -her  to-do list is still there

#Satisfied,she goes back to sleep
brower.quit()
