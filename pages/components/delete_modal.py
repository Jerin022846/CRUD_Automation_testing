from selenium.webdriver.common.by import By
from utils.waits import wait_visible

class DeleteModal:
    ROOT    = (By.XPATH, "//div[contains(@class,'oxd-dialog-container')]//div[contains(@class,'oxd-dialog')]")
    CONFIRM = (By.XPATH, "//button[normalize-space()='Yes, Delete']")
    CANCEL  = (By.XPATH, "//button[normalize-space()='No, Cancel']")

    @staticmethod
    def confirm(driver):
        wait_visible(driver, DeleteModal.ROOT)
        driver.find_element(*DeleteModal.CONFIRM).click()

