from selenium import webdriver

options = webdriver.firefox.options.Options()
options.add_argument("-profile")
options.add_argument("/home/rainer/snap/firefox/common/.mozilla/firefox/d6rakj4m.default-release")

browser = webdriver.Firefox(options=options)
browser.get('http://localhost:8000')

assert 'Django' in browser.title
