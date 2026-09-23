from selenium.webdriver.common.by import By
from .base_page import BasePage
from utils.waits import wait_clickable, wait_visible, wait_spinners_gone, wait_url_contains 

class Sidebar(BasePage):
    SHELL = (By.CSS_SELECTOR, "aside.oxd-sidepanel")
    PIM_MENU = (By.XPATH, "//span[normalize-space()='PIM']/ancestor::a")

    def goto_pim(self):
        wait_visible(self.driver, self.SHELL)
        wait_clickable(self.driver, self.PIM_MENU).click()
        wait_url_contains(self.driver, "/pim/viewEmployeeList")
        wait_spinners_gone(self.driver, timeout=8)