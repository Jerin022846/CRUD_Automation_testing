from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from .base_page import BasePage
from utils.waits import wait_clickable, wait_visible, wait_all_visible, wait_spinners_gone, human_pause

from utils.waits import (
    wait_clickable, wait_visible, wait_all_visible,
    wait_spinners_gone, wait_url_contains
)
from pages.components.delete_modal import DeleteModal

class PimListPage(BasePage):
    # Top “Add” button
    ADD_BTN = (By.XPATH, "//button[.//i[contains(@class,'bi-plus')] or normalize-space()='Add']")

    # Search panel
    EMP_ID_INPUT = (By.XPATH, "//label[normalize-space()='Employee Id']/../following-sibling::div//input")
    SEARCH_BTN   = (By.XPATH, "//button[normalize-space()='Search']")
    RESET_BTN    = (By.XPATH, "//button[normalize-space()='Reset']")

    # Table results
    TABLE_BODY   = (By.CSS_SELECTOR, "div.oxd-table-body")
    TABLE_ROWS   = (By.CSS_SELECTOR, "div.oxd-table-body > div.oxd-table-card")
    NO_RECORDS   = (By.XPATH, "//span[normalize-space()='No Records Found']")

    # Row actions
    FIRST_ROW    = (By.CSS_SELECTOR, "div.oxd-table-body > div.oxd-table-card:first-child")
    FIRST_DELETE = (By.CSS_SELECTOR, "div.oxd-table-body > div.oxd-table-card:first-child i.bi-trash")

    def __init__(self, driver):
        self.driver = driver

    # --- Add employee flow ---
    def add_employee(self):
        wait_spinners_gone(self.driver, timeout=6)
        btn = wait_clickable(self.driver, self.ADD_BTN, timeout=20)
        human_pause(self.driver, 200)
        btn.click()
        wait_spinners_gone(self.driver, timeout=6)

    # --- Search flow ---
    def search_by_id(self, emp_id: str):
        wait_spinners_gone(self.driver, timeout=6)
        # Clear previous filter to avoid stale state
        wait_clickable(self.driver, self.RESET_BTN, timeout=10).click()
        wait_spinners_gone(self.driver, timeout=6)

        box = wait_visible(self.driver, self.EMP_ID_INPUT, timeout=20)
        box.clear()
        box.send_keys(emp_id)
        human_pause(self.driver, 180)
        wait_clickable(self.driver, self.SEARCH_BTN, timeout=10).click()
        wait_spinners_gone(self.driver, timeout=12)

        # Wait until either rows load or "No Records Found" appears
        try:
            wait_visible(self.driver, self.TABLE_BODY, timeout=10)
        except Exception:
            # Some builds skip the body visibility; continue to counting section
            pass

        return self.results_count()  # so tests can assert count

    def results_count(self) -> int:
        rows = self.driver.find_elements(*self.TABLE_ROWS)
        if rows:
            return len(rows)
        # If no rows, check for "No Records Found"
        empty = self.driver.find_elements(*self.NO_RECORDS)
        return 0 if empty else 0

    def open_first_result(self):
        wait_visible(self.driver, self.FIRST_ROW, timeout=15)
        human_pause(self.driver, 150)
        self.driver.find_element(*self.FIRST_ROW).click()
        wait_spinners_gone(self.driver, timeout=8)

    def delete_first_result(self):
        wait_visible(self.driver, self.FIRST_ROW, timeout=15)
        human_pause(self.driver, 150)
        self.driver.find_element(*self.FIRST_DELETE).click()
        wait_spinners_gone(self.driver, timeout=4)