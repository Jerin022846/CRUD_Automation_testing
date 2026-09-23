from selenium.webdriver.common.by import By
from .base_page import BasePage

class AddEmployeePage(BasePage):
    FIRST_NAME  = (By.XPATH, "//input[@placeholder='First Name']")
    MIDDLE_NAME = (By.XPATH, "//input[@placeholder='Middle Name']")
    LAST_NAME   = (By.XPATH, "//input[@placeholder='Last Name']")
    EMPLOYEE_ID = (By.XPATH, "//label[normalize-space()='Employee Id']/following::input[1]")
    SAVE_BTN    = (By.XPATH, "//button[normalize-space()='Save']")

    def fill(self, first, middle, last, emp_id=None):
        self.type(self.FIRST_NAME, first)
        self.type(self.MIDDLE_NAME, middle)
        self.type(self.LAST_NAME, last)
        if emp_id is not None:
            self.type(self.EMPLOYEE_ID, emp_id)

    def save(self):
        self.click(self.SAVE_BTN)

