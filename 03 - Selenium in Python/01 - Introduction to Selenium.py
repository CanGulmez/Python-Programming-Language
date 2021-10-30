from selenium import webdriver

driver = webdriver.Chrome("C:/Users/90545/MyStudies/01 - Python Programming Language/03 - Selenium in Python/chromedriver.exe")

url = "https://github.com/CanGulmez"

driver.get(url)      # get method opens web page.