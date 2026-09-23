from selenium.webdriver.common.by import By
from utils.waits import wait_visible

class Toast:
    SUCCESS = (By.XPATH, "//div[contains(@class,'oxd-toast')][.//*[contains(normalize-space(.),'Success')]]")
    @staticmethod
    def wait_success(driver):
        return wait_visible(driver, Toast.SUCCESS)

