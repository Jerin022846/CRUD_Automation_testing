from selenium.webdriver.common.by import By
from utils.waits import wait_url_contains
from .base_page import BasePage

class LoginPage(BasePage):
    USERNAME = (By.XPATH, "//input[@placeholder='Username']")
    PASSWORD = (By.XPATH, "//input[@placeholder='Password']")
    SUBMIT   = (By.XPATH, "//button[normalize-space()='Login']")

    def open(self, base_url):
        self.driver.get(base_url)
        return self

    def login(self, username, password):
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.click(self.SUBMIT)
        wait_url_contains(self.driver, "/index")

