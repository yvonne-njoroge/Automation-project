# pages/login_page.py
from selenium.webdriver.common.by import By

class LoginPage:
    username = (By.ID, "username")
    password = (By.ID, "password")
    login_btn = (By.ID, "submit")

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get("https://practicetestautomation.com/practice-test-login/")

    def login(self, user, pwd):
        self.driver.find_element(*self.username).send_keys(user)
        self.driver.find_element(*self.password).send_keys(pwd)
        self.driver.find_element(*self.login_btn).click()