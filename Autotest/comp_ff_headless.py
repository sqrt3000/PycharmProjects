"""
Заходим на сайт front.comparium.app
вставляем тестируемый адрес, выбираем все капабилити, жмем генерацию скринов,
делаем скрин, сохраняем скрин,
открываем новую вкладку, проделываем те же операции.
"""
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import time

opts = Options()
opts.add_argument('-headless')
PROXY_HOST = '192.168.3.2'  # rotating proxy or host
PROXY_PORT = 8080 # port
PROXY_USER = 'proxy-user' # username
PROXY_PASS = 'proxy-password' # password


def test(url, test_url, passes):
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
        inp = browser.find_element_by_xpath(
            "//*[@id='gatsby-focus-wrapper']/main/div[1]/form/div[1]/input")
        time.sleep(1)
        print('delay 1 s for load web.app')
        inp.click()
        print('Ckick on input and get menu config')
        inp_set = browser.find_element_by_xpath(
            "//*[@id='gatsby-focus-wrapper']/main/div[1]/form/div[1]/input")
        inp_set.send_keys(test_url)
        print('Set URL in field "Input URL"')
        select1 = browser.find_element_by_xpath(
            "//*[@id='gatsby-focus-wrapper']/main/div[1]/form/div[2]/table/tbody/tr[2]/td[2]/label[1]")
        select2 = browser.find_element_by_xpath(
            "//*[@id='gatsby-focus-wrapper']/main/div[1]/form/div[2]/table/tbody/tr[2]/td[2]/label[2]")
        select3 = browser.find_element_by_xpath(
            "//*[@id='gatsby-focus-wrapper']/main/div[1]/form/div[2]/table/tbody/tr[2]/td[3]/label[1]")
        select4 = browser.find_element_by_xpath(
            "//*[@id='gatsby-focus-wrapper']/main/div[1]/form/div[2]/table/tbody/tr[2]/td[3]/label[2]")
        select5 = browser.find_element_by_xpath(
            "//*[@id='gatsby-focus-wrapper']/main/div[1]/form/div[2]/table/tbody/tr[2]/td[4]/label[1]")
        select6 = browser.find_element_by_xpath(
            "//*[@id='gatsby-focus-wrapper']/main/div[1]/form/div[2]/table/tbody/tr[2]/td[4]/label[2]")
        select7 = browser.find_element_by_xpath(
            "//*[@id='gatsby-focus-wrapper']/main/div[1]/form/div[2]/table/tbody/tr[2]/td[6]/label[1]")
        select8 = browser.find_element_by_xpath(
            "//*[@id='gatsby-focus-wrapper']/main/div[1]/form/div[2]/table/tbody/tr[2]/td[6]/label[2]")
        select9 = browser.find_element_by_xpath(
            "//*[@id='gatsby-focus-wrapper']/main/div[1]/form/div[2]/table/tbody/tr[3]/td[2]/label[1]")
        select10 = browser.find_element_by_xpath(
            "//*[@id='gatsby-focus-wrapper']/main/div[1]/form/div[2]/table/tbody/tr[3]/td[2]/label[2]")
        select11 = browser.find_element_by_xpath(
            "//*[@id='gatsby-focus-wrapper']/main/div[1]/form/div[2]/table/tbody/tr[3]/td[3]/label[1]")
        select12 = browser.find_element_by_xpath(
            "//*[@id='gatsby-focus-wrapper']/main/div[1]/form/div[2]/table/tbody/tr[3]/td[3]/label[2]")
        select13 = browser.find_element_by_xpath(
            "//*[@id='gatsby-focus-wrapper']/main/div[1]/form/div[2]/table/tbody/tr[3]/td[5]/label")
        select14 = browser.find_element_by_xpath(
            "//*[@id='gatsby-focus-wrapper']/main/div[1]/form/div[2]/table/tbody/tr[3]/td[6]/label[1]")
        select15 = browser.find_element_by_xpath(
            "//*[@id='gatsby-focus-wrapper']/main/div[1]/form/div[2]/table/tbody/tr[3]/td[6]/label[2]")
        select16 = browser.find_element_by_xpath(
            "//*[@id='gatsby-focus-wrapper']/main/div[1]/form/div[2]/table/tbody/tr[4]/td[2]/label")
        select17 = browser.find_element_by_xpath(
            "//*[@id='gatsby-focus-wrapper']/main/div[1]/form/div[2]/table/tbody/tr[4]/td[3]/label")
        select18 = browser.find_element_by_xpath(
            "//*[@id='gatsby-focus-wrapper']/main/div[1]/form/div[2]/table/tbody/tr[5]/td[2]/label[1]")
        select19 = browser.find_element_by_xpath(
            "//*[@id='gatsby-focus-wrapper']/main/div[1]/form/div[2]/table/tbody/tr[5]/td[2]/label[2]")
        select20 = browser.find_element_by_xpath(
            "//*[@id='gatsby-focus-wrapper']/main/div[1]/form/div[2]/table/tbody/tr[5]/td[3]/label[1]")
        select21 = browser.find_element_by_xpath(
            "//*[@id='gatsby-focus-wrapper']/main/div[1]/form/div[2]/table/tbody/tr[5]/td[3]/label[2]")
        select22 = browser.find_element_by_xpath(
            "//*[@id='gatsby-focus-wrapper']/main/div[1]/form/div[2]/table/tbody/tr[5]/td[6]/label")
        select1.click()
        select2.click()
        select3.click()
        select4.click()
        select5.click()
        select6.click()
        select7.click()
        select8.click()
        select9.click()
        select10.click()
        select11.click()
        select12.click()
        select13.click()
        select14.click()
        select15.click()
        select16.click()
        select17.click()
        select18.click()
        select19.click()
        select20.click()
        select21.click()
        select22.click()
        print('Select all config')
        btn = browser.find_element_by_xpath(
            "//*[@id='gatsby-focus-wrapper']/main/div[1]/form/div[2]/table/tbody/tr[6]/td[2]")
        print('Click button CREATE SCREENS')
        btn.click()
        browser.save_screenshot(f"./Screenshots/screenshot_{i}.png")
        print('Make screenshot and save it')
        browser.execute_script(f"window.open('{url}','_blank');")
        print('Open new tab')
        browser.switch_to.window(browser.window_handles[i])
        i += 1
    print('delay 10 s')
    time.sleep(10)
    print('Close browser')
    browser.close()


url = 'https://front.comparium.app/'
test_url = 'https://comparium.app'
passes = 3

test(url, test_url, passes)




