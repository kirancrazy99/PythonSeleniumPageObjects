import pytest
from BasePage import Basepage
from selenium import webdriver
driver = webdriver.Chrome()

class RegistrationPage(Basepage):

    def __init__(self, driver):
        super().__init__(driver)

    def fill_form(self,name,email,phone,city,country,username,password):
        self.type_element("name_Xpath", name)
        self.type_element("phone_XPath", phone)
        self.type_element("email_Xpath", email)
        self.type_element("city_Xpath", city)
        self.select("country_Xpath", country)
        self.type_element("username_Xpath", username)
        self.type_element("password_Xpath", password)
        self.click('submit_Xpath')


rg = RegistrationPage(driver)



