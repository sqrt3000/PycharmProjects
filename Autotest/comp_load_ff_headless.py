from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import time

opts = Options()
opts.add_argument('-headless')
PROXY_HOST = '192.168.3.2'  # rotating proxy or host
PROXY_PORT = 8080 # port
PROXY_USER = 'proxy-user' # username
PROXY_PASS = 'proxy-password' # password


def test(url, passes):
    opts.set_preference("dom.popup_maximum", passes)
    browser = Firefox(options=opts)
    print('**************************')
    print('Open browser')
    i = 0
    while i <= passes:
        print('-------------------------------')
        print(f"Iteration number {i}")
        print('-------------------------------')
        browser.get(url)
        print('Get URl')
        # browser.save_screenshot(f"./Screenshots/screenshot_{i}.png")
        # print('Make screenshot and save it')
        browser.execute_script(f"window.open('{url}','_blank');")
        print('Open new tab')
        browser.switch_to.window(browser.window_handles[i])
        i += 1
    print('delay 10 s')
    time.sleep(10)
    print('Close browser')
    browser.close()
    browser.quit()


url = 'https://front.comparium.app/'
passes = 50

test(url, passes)




