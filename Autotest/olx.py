from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

opts = Options()

browser = Firefox(options=opts)
browser.get('https://www.olx.ua/')
browser.find_element_by_tag_name('span').click()
