from selenium import webdriver
import time 
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("C:/Users/90545/MyStudies/01 - Python Programming Language/03 - Selenium in Python/chromedriver.exe")
url = "http://github.com"

driver.get(url)
driver.maximize_window()

searchInput = driver.find_element_by_xpath("/html/body/div[1]/header/div/div[2]/div[2]/div[2]/a")
searchInput.send_keys(Keys.ENTER)

def check_username_password():

    username = ""
    password = ""

    searchInput_ = driver.find_element_by_xpath("//*[@id='login_field']")
    searchInput_1 = driver.find_element_by_xpath("//*[@id='password']")

    if searchInput_ == username and searchInput_1 == password:

        searchInput_.send_keys(Keys.ENTER)
        searchInput_1.send_keys(Keys.ENTER)

    else:
        searchInput_.send_keys(username)
        searchInput_1.send_keys(password)

check_username_password()

searchInput_2 = driver.find_element_by_xpath("//*[@id='login']/div[4]/form/div/input[12]")
searchInput_2.send_keys(Keys.ENTER)

url_ = "https://github.com/CanGulmez"

driver.get(url_)

searchInput_3 = driver.find_element_by_xpath("//*[@id='js-pjax-container']/div[1]/div/div/div[2]/div/nav/a[2]")
searchInput_3.send_keys(Keys.ENTER)

driver.close()