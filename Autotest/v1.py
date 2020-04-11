# https://realpython.com/modern-web-automation-with-python-and-selenium/

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

opts = Options()

browser = Firefox(options=opts)
browser.get('https://bandcamp.com')
browser.find_element_by_class_name('playbutton').click()

# tracks = browser.find_elements_by_class_name('discover-item')
# len(tracks)  # 8
# tracks[3].click()
