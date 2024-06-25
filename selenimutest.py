from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

#
url = 'https://tw.stock.yahoo.com/intl-markets/'
driver.get(url)

#捲動視窗
js = "window.scrollTo(0, document.body.scrollHeight);"
driver.execute_script(js)
time.sleep(5)

elems = driver.find_elements(By.CSS_SELECTOR, '[class*="Mt(0)"][class*="Mb(8px)"]')
# print(len(elems))

for elem in elems:
    title = elem.text
    elem = elem.find_element(By.TAG_NAME, 'a')
    href = elem.get_attribute('href')
    # 輸出標題和網址
    print('_' * 35)
    print("標題:", title)
    # print("網址:", href)

driver.quit()