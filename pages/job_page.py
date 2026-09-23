from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from .base_page import BasePage
from utils.waits import wait_visible, wait_clickable, wait_spinners_gone


class JobPage(BasePage):
    # Fields on the Job tab
    JOINED_DATE = (By.XPATH, "//label[normalize-space()='Joined Date']/following::input[1]")
    JOB_TITLE   = (By.XPATH, "//label[normalize-space()='Job Title']/following::div[contains(@class,'oxd-select-text')][1]")
    SUB_UNIT    = (By.XPATH, "//label[normalize-space()='Sub Unit']/following::div[contains(@class,'oxd-select-text')][1]")
    EMP_STATUS  = (By.XPATH, "//label[normalize-space()='Employment Status']/following::div[contains(@class,'oxd-select-text')][1]")

    SAVE_BTN    = (By.XPATH, "//form[.//label[normalize-space()='Joined Date']]//button[normalize-space()='Save']")

    def _select_dd(self, dropdown_locator, option_text: str):
        """Open an OrangeHRM oxd select and pick an exact option by visible text."""
        dd = wait_clickable(self.driver, dropdown_locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", dd)
        dd.click()
        option = (By.XPATH, f"//div[@role='listbox']//*[normalize-space()='{option_text}']")
        wait_clickable(self.driver, option).click()

    def update_job(self, joined_date: str, job_title: str, sub_unit: str, emp_status: str):
        """Update Job tab fields and click Save."""
        # Joined Date – clear thoroughly, then set yyyy-mm-dd
        date_input = wait_visible(self.driver, self.JOINED_DATE)
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", date_input)
        date_input.click()
        # Close calendar if open and ensure focus is correct, then clear
        date_input.send_keys(Keys.TAB)
        date_input.click()
        date_input.send_keys(Keys.CONTROL, "a")
        date_input.send_keys(Keys.BACKSPACE)
        date_input.send_keys(joined_date)

        # Dropdowns
        self._select_dd(self.JOB_TITLE, job_title)
        self._select_dd(self.SUB_UNIT, sub_unit)
        self._select_dd(self.EMP_STATUS, emp_status)

        # Save and wait for UI to settle
        wait_clickable(self.driver, self.SAVE_BTN).click()
        try:
            wait_spinners_gone(self.driver, timeout=10)
        except Exception:
            # Spinner may be brief; ignore if not present
            pass

        return self