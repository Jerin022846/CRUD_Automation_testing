from selenium.webdriver.common.by import By
from .base_page import BasePage

class SalaryPage(BasePage):
    ADD_BTN       = (By.XPATH, "//button[normalize-space()='Add']")
    COMPONENT     = (By.XPATH, "//label[normalize-space()='Salary Component']/following::input[1]")
    PAY_GRADE     = (By.XPATH, "//label[normalize-space()='Pay Grade']/following::div[contains(@class,'oxd-select-text')]")
    CURRENCY      = (By.XPATH, "//label[normalize-space()='Currency']/following::div[contains(@class,'oxd-select-text')]")
    AMOUNT        = (By.XPATH, "//label[normalize-space()='Amount']/following::input[1]")
    COMMENTS      = (By.XPATH, "//label[normalize-space()='Comments']/following::textarea[1]")
    SAVE_BTN      = (By.XPATH, "//button[normalize-space()='Save']")

    def _select(self, locator, text):
        self.click(locator)
        self.click((By.XPATH, f"//div[@role='listbox']//*[normalize-space()='{text}']"))

    def add_salary(self, component, pay_grade, currency, amount, comments=""):
        self.click(self.ADD_BTN)
        self.type(self.COMPONENT, component)
        self._select(self.PAY_GRADE, pay_grade)
        self._select(self.CURRENCY, currency)
        self.type(self.AMOUNT, str(amount))
        if comments:
            self.type(self.COMMENTS, comments)
        self.click(self.SAVE_BTN)

