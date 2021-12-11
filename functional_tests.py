from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = True

browser = webdriver.Firefox(options=options, executable_path=r"/workspace/python-TDD-book-examples/geckodriver")
browser.get('http://localhost:8000')

assert 'Django' in browser.title