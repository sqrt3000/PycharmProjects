"""
Скрипт принимает url и разрешение экрана (ширину) и генерирует
на выходе файл - скриншот в формате png. Скрол убран.
Длинные страницы успешно скринятся без склейки,
включая полный футер.
FireFox.
"""
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import time

opts = Options()
opts.add_argument('-headless')
opts.add_argument('--start-maximized')

PROXY_HOST = '192.168.3.2'  # rotating proxy or host
PROXY_PORT = 8080 # port
PROXY_USER = 'proxy-user'   # username
PROXY_PASS = 'proxy-password'   # password

path = str("./Screenshots/screenshot.png")


def test(test_url):
    print('**************************')
    print('Open browser')
    browser = Firefox(options=opts)
    browser.set_window_size(375, 0)
    print('Get URl')
    browser.get(test_url)
    total_width = browser.execute_script("return document.body.offsetWidth")
    total_height = browser.execute_script("return document.body.scrollHeight")
    print('Scrolling...')
    browser.set_window_size(total_width, total_height+83)
    print('Set window size...')
    print('Delay 2 s')
    time.sleep(2)
    browser.find_element_by_tag_name('body').screenshot(path)
    print('Make screenshot and save it')
    browser.close()
    browser.quit()
    print('Close browser')


# test_url = 'https://habr.com/ru/post/474450/'
# test_url = 'https://stackoverflow.com/questions/41721734/take-screenshot-of-full-page-with-selenium-python-with-chromedriver'
# test_url = 'https://stackoverflow.com/questions/28431765/open-web-in-new-tab-selenium-python'
test_url = 'https://comparium.app/internet-explorer-for-mac.html'
# test_url = 'https://stackoverflow.com/questions/41721734/take-screenshot-of-full-page-with-selenium-python-with-chromedriver'
test(test_url)

