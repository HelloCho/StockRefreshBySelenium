from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument('ignore-certificate-errors')
options.add_argument("--disable-infobars")

browser = webdriver.Chrome('/Applications/chromedriver_mac64_87/chromedriver',chrome_options=options)
browser.get('https://finance.naver.com/item/main.nhn?code=066970')

clickNewsButton = browser.find_element_by_css_selector('#content > ul > li:nth-child(5) > a > span')
clickNewsButton.click()

clickChartButton = browser.find_element_by_css_selector('#btn_close > img')
clickChartButton.click()

try:
    # start
    while True:
        time.sleep(60)
        browser.refresh()
        time.sleep(2)
        clickChartButton = browser.find_element_by_css_selector('#btn_close > img')
        clickChartButton.click()

except:
    print('Error...')

finally:
    browser.close()