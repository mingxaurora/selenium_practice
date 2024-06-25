from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

#在瀏覽器中開啟以下網頁
url = 'https://tw.stock.yahoo.com/intl-markets/'
driver.get(url)

#捲動視窗
js = "window.scrollTo(0, document.body.scrollHeight);"
driver.execute_script(js)
time.sleep(5)  #等待頁面更新

#以元素屬性－class=Mt(0) Mb(8px) 作搜尋
elems = driver.find_elements(By.CSS_SELECTOR, '[class*="Mt(0)"][class*="Mb(8px)"]')
# print(len(elems))

#逐一顯示搜尋到的內容－新聞標題與連結
for elem in elems:
    title = elem.text
    elem = elem.find_element(By.TAG_NAME, 'a')
    href = elem.get_attribute('href')
    # 輸出標題和網址
    print('_' * 35)
    print("標題:", title)
    print("網址:", href)

driver.quit()
