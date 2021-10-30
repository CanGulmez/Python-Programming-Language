from selenium import webdriver
import time 
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("C:/Users/90545/MyStudies/01 - Python Programming Language/03 - Selenium in Python/chromedriver.exe")

url = "http://github.com"

driver.get(url)
driver.maximize_window()

time.sleep(1)

searchInput = driver.find_element_by_name("q")
searchInput.send_keys("CanGulmez")

time.sleep(1)

searchInput.send_keys(Keys.ENTER)

time.sleep(1)

# result = driver.page_source
# print(result)

searchInput_ = driver.find_element_by_xpath("//*[@id='js-pjax-container']/div/div[2]/nav[1]/a[10]")
searchInput_.send_keys(Keys.ENTER)

# driver.close()