from bs4 import BeautifulSoup
from urllib import request





url = 'https://www.starbucks.co.kr/store/store_map.do'

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get(url)
time.sleep(5)

page = driver.page_source
soup = BeautifulSoup(page,'html.parser')
print(soup.select('ul.quickSearchResultBox li'))
