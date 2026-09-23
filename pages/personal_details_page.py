from selenium.webdriver.common.by import By
from .base_page import BasePage
from utils.waits import wait_visible, wait_clickable, wait_spinners_gone
import time
from selenium.webdriver.common.keys import Keys

class PersonalDetailsPage(BasePage):

    # Name near avatar
    NAME_BOX = (By.XPATH, "//div[contains(@class,'orangehrm-edit-employee-name')]")
    HEADER_NAME_H6 = (By.XPATH, "(//div[contains(@class,'orangehrm-edit-employee-name')]//h6)[1]")

    OTHER_ID    = (By.XPATH, "//label[normalize-space()='Other Id']/following::input[1]")
    NATIONALITY = (By.XPATH, "//label[normalize-space()='Nationality']/following::div[contains(@class,'oxd-select-text')][1]")
    MARITAL     = (By.XPATH, "//label[normalize-space()='Marital Status']/following::div[contains(@class,'oxd-select-text')][1]")
    DOB         = (By.XPATH, "//label[normalize-space()='Date of Birth']/following::input[1]")
    GENDER_MALE = (By.XPATH, "//label[normalize-space()='Male']")
    GENDER_FEMALE = (By.XPATH, "//label[normalize-space()='Female']")
    SAVE_BTN    = (By.XPATH, "//form[.//label[normalize-space()='Other Id'] or .//label[normalize-space()='Nationality']]//button[normalize-space()='Save']")

    # Key field to prove the Personal Details form loaded
    EMPLOYEE_ID_INPUT = (By.XPATH, "//label[normalize-space()='Employee Id']/following::input[1]")

    JOB_TAB     = (By.XPATH, "//a[normalize-space()='Job']")
    SALARY_TAB  = (By.XPATH, "//a[normalize-space()='Salary']")

    def header_name(self):
        # Wait for the name container, then read textContent to avoid empty .text timing issues
        wait_visible(self.driver, self.NAME_BOX)
        el = self.driver.find_element(*self.HEADER_NAME_H6)
        txt = (el.get_attribute("textContent") or "").strip()
        return txt

    def get_employee_id(self) -> str:
        el = wait_visible(self.driver, self.EMPLOYEE_ID_INPUT)
        return (el.get_attribute("value") or el.get_property("value") or "").strip()

    def _select_from_dropdown(self, dropdown_locator, option_text):
        self.click(dropdown_locator)
        option = (By.XPATH, f"//div[@role='listbox']//*[normalize-space()='{option_text}']")
        self.click(option)

    def set_personal_details(self, other_id, nationality, marital, dob, gender='Male'):
        self.type(self.OTHER_ID, other_id)
        self._select_from_dropdown(self.NATIONALITY, nationality)
        self._select_from_dropdown(self.MARITAL, marital)
        self.type(self.DOB, dob)
        el = wait_visible(self.driver, self.DOB)
        el.send_keys(Keys.TAB)
        if gender:
            if gender.lower().startswith("m"):
               el = wait_clickable(self.driver, self.GENDER_MALE)
            else:
               el = wait_clickable(self.driver, self.GENDER_FEMALE)
            try:
               el.click()
            except Exception:
                   self.driver.execute_script("arguments[0].click();", el)
    
        save = wait_clickable(self.driver, self.SAVE_BTN)
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", save)
        try:
           save.click()
        except Exception:
           self.driver.execute_script("arguments[0].click();", save)
    
    def goto_job(self):
        self.click(self.JOB_TAB)

    def goto_salary(self):
        self.click(self.SALARY_TAB)
    
    def get_employee_id(self) -> str:
        el = wait_visible(self.driver, self.EMPLOYEE_ID_INPUT)
    # wait up to ~5s until the auto-generated ID appears
        for _ in range(10):
           value = el.get_attribute("value") or ""
           if value.strip():
              return value.strip()
           time.sleep(0.5)
        return ""
