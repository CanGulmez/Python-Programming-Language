from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

class Selenium:

    def __init__(self):

        self.browser = webdriver.Chrome("C:/Users/90545/MyStudies/01 - Python Programming Language/03 - Selenium in Python/chromedriver.exe")

    def getDocumantation(self):

        self.browser.get("https://selenium-python.readthedocs.io/")
        self.browser.maximize_window()

        self.browser.find_element_by_xpath("//*[@id='selenium-with-python']/div[2]/ul/li[1]/a").send_keys(Keys.ENTER)

        installation = self.browser.find_element_by_class_name("section").text
        print("------------------------------------------------------------------------------------------")
        print(installation)
        print("------------------------------------------------------------------------------------------")

        self.browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/ul/li[2]/a").send_keys(Keys.ENTER)

        gettingStarted = self.browser.find_element_by_id("getting-started").text
        print("------------------------------------------------------------------------------------------")
        print(gettingStarted)
        print("------------------------------------------------------------------------------------------")

        self.browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/ul/li[3]/a").send_keys(Keys.ENTER)

        navigating = self.browser.find_element_by_class_name("body").text
        print("------------------------------------------------------------------------------------------")
        print(navigating)
        print("------------------------------------------------------------------------------------------")

        self.browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/ul/li[4]/a").send_keys(Keys.ENTER)

        locatingElements = self.browser.find_element_by_id("locating-elements").text
        print("------------------------------------------------------------------------------------------")
        print(locatingElements)
        print("------------------------------------------------------------------------------------------")

        self.browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/ul/li[5]/a").send_keys(Keys.ENTER)

        waits = self.browser.find_element_by_id("waits").text
        print("------------------------------------------------------------------------------------------")
        print(waits)
        print("------------------------------------------------------------------------------------------")

        self.browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/ul/li[6]/a").send_keys(Keys.ENTER)

        pageObjects = self.browser.find_element_by_id("page-objects").text
        print("------------------------------------------------------------------------------------------")
        print(pageObjects)
        print("------------------------------------------------------------------------------------------")

        self.browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/ul/li[7]/a").send_keys(Keys.ENTER)

        webdriverAPI = self.browser.find_element_by_id("webdriver-api").text
        print("------------------------------------------------------------------------------------------")
        print(webdriverAPI)
        print("------------------------------------------------------------------------------------------")

        self.browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/ul/li[8]/a").send_keys(Keys.ENTER)

        appendix = self.browser.find_element_by_id("appendix-frequently-asked-questions").text
        print("------------------------------------------------------------------------------------------")
        print(appendix)
        print("------------------------------------------------------------------------------------------")


seleniumDemo = Selenium()
seleniumDemo.getDocumantation()