from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = True

browser = webdriver.Firefox(options=options, executable_path=r"/workspace/python-TDD-book-examples/geckodriver")

# Edith has heard about a cool new online to-do app.  She goes
# to check out its homepage
browser.get('http://localhost:8000')

# She notices the page title and header mention to-do lists
assert 'To-Do' in browser.title

# She is invited to enter a to-do item straight away

# She types "Buy peacock feathers" into a text box (Edith's hobby
# is tying fly-fishing lures)

# When she hits enter, the page updates, and now the page lists
# "1: Buy peacock feathers" as an item in a to-do list

# There is still a text box in inviting her to add another item.  She
# enters "Use peacock feathers to make a fly" (Edith is very methodical)

# The page updates afain, and now shows both items on her list

#Edith wonders whether the site will remember her list.  Then she sees
# that the site has generated a unique URL for her -- there is some
# explanatory text to that effect.

# Sher visits that URL - her to-do list is still there.

# Satsfied, she goes back to sleep

browser.quit()
