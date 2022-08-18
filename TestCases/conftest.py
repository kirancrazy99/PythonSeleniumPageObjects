from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
# import pytest
from ConfigReader.con_file import conf_reader
import time

def get_browser():
    driver = webdriver.Chrome()
    url = conf_reader('base info','testsiteurl')
    print(url)
    driver.get('https://qa.way2automation.com')
    # driver.get(url=url)
    driver.maximize_window()
    # time.sleep(5)
    return driver
    # driver.quit()

get_browser()