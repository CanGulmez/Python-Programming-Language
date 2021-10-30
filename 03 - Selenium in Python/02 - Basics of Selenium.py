from selenium import webdriver
import time

driver = webdriver.Chrome("C:/Users/90545/MyStudies/01 - Python Programming Language/03 - Selenium in Python/chromedriver.exe")

url = "https://github.com/CanGulmez"
driver.get(url)                           # opens web page.

driver.maximize_window()                  # expands the screen.
driver.save_screenshot("github.png")      # saves screenshot
time.sleep(2)                             # waits for 2 second while the page is open.
print(driver.title)                       # prints page's title.
# time.sleep(2)                           # waits for 2 second while the page is open.

url_ = "https://github.com"
driver.get(url_)

time.sleep(2)

driver.back()                             # forward ==> ileri, back ==> geri

time.sleep(2)

if "CanGulmez" in driver.title:
    driver.save_screenshot("github-CanGulmez.png")

driver.close()                            # closes the page that opened.