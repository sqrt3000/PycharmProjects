from selenium import webdriver
import time

# options = webdriver.ChromeOptions()
# options.add_argument('headless')
# options.add_argument('window-size=1366x876') #Можно установить конкретное разрешение экрана

PROXY_HOST = '192.168.3.2'  # rotating proxy or host
PROXY_PORT = 8080 # port
PROXY_USER = 'proxy-user' # username
PROXY_PASS = 'proxy-password' # password

url = 'https://www.myip.com/'
passes = 10


def test(url, passes):
    browser = webdriver.Chrome('./chromedriver')
    # browser = webdriver.Chrome(chrome_options=options)
    i = 0
    while i <= passes:
        i += 1
        print(i)
        print('Open browser')
        browser.get(url)
        print('YouTube')
        time.sleep(2)
        print('delay 2 s')

        # btn = browser.find_element_by_xpath("//*[@id='movie_player']/div[5]/button")
        # print('Click button Play')
        # btn.click()

        browser.execute_script(f"window.open('{url}','_blank');")
        browser.switch_to.window(browser.window_handles[i])

    browser.close()
    browser.quit()
    print('Close browser')


test(url, passes)




