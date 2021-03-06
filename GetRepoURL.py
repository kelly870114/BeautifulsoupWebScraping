from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
 
 
options = Options()
#options.add_argument("--disable-notifications")  # 取消所有的alert彈出視窗
 
browser = webdriver.Chrome(
    ChromeDriverManager().install(), chrome_options=options)
 
browser.get("https://github.com/topics/android")
 

 
for page in range(1, 3):  # 執行1~2頁

    page_next = browser.find_element_by_xpath('//button[@class="ajax-pagination-btn btn btn-outline color-border-default f6 mt-0 width-full"]')
    page_next.click()  # 點擊下一頁按鈕
 
    time.sleep(5)  # 暫停10秒
    
soup = BeautifulSoup(browser.page_source, "html.parser")
 
# 取得所有class為text-bold wb-break-word的<a>標籤
elements = soup.find_all("a", {"class": "text-bold wb-break-word"})
 
#print(f"==========第{str(page)}頁==========")
for element in elements:
    # 取得<a>標籤下的href
    title = element.get('href')
    #印出url(避免url中間有空格，所以用%)
    print("https://github.com%s"%title)
