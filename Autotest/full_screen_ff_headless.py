from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import time

opts = Options()
opts.add_argument('-headless')
PROXY_HOST = '192.168.3.2'  # rotating proxy or host
PROXY_PORT = 8080 # port
PROXY_USER = 'proxy-user' # username
PROXY_PASS = 'proxy-password' # password


def test(test_url):
    browser = Firefox(options=opts)
    print('**************************')
    print('Open browser')
    browser.get(test_url)
    print('Get URl')
    print('delay 7 s')
    time.sleep(7)
    total_width = browser.execute_script("return document.body.offsetWidth")
    total_height = browser.execute_script(f"return document.body.scrollHeight")
    browser.set_window_size(total_width, total_height+83)
    browser.save_screenshot(f"./Screenshots/screenshot.png")
    print('Make screenshot and save it')
    browser.close()
    browser.quit()
    print('Close browser')


test_url = 'https://habr.com/ru/post/474450/'
test(test_url)

