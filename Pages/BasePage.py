from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from ConfigReader import con_file


class Basepage:

    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        self.driver.find_element(by=By.XPATH, value=con_file.conf_reader('locators', locator)).click()

    def type_element(self, locator, value):
        self.driver.find_element(by=By.XPATH, value=con_file.conf_reader('locators', locator)).send_keys(value)

    def select(self, locator, value):
        dropdown = self.driver.find_element(by=By.XPATH, value=con_file.conf_reader('locators', locator))
        select = Select(dropdown)
        select.select_by_visible_text(value)
