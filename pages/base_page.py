import time
from utils.waits import wait_clickable, wait_visible

# -------------------------------------------------------------------
# GLOBAL ACTION SPEED SETTINGS
# -------------------------------------------------------------------
ACTION_DELAY = 0.4     # pause (in seconds) after each click/type
TYPE_DELAY = 0.1       # delay between each keystroke (for human typing)
# -------------------------------------------------------------------

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, by_locator):
        """Click an element once it's clickable, then pause briefly."""
        el = wait_clickable(self.driver, by_locator)
        el.click()
        time.sleep(ACTION_DELAY)  # 👈 pause after every click
        return el

    def type(self, by_locator, text, clear=True):
        """Type text like a human — character by character."""
        el = wait_visible(self.driver, by_locator)
        if clear:
            el.clear()
            time.sleep(0.2)  # slight pause after clearing

        for char in str(text):
            el.send_keys(char)
            time.sleep(TYPE_DELAY)  # 👈 simulate human typing speed

        time.sleep(ACTION_DELAY)  # pause after completing typing
        return el

    def text_of(self, by_locator):
        """Get visible text of an element."""
        el = wait_visible(self.driver, by_locator)
        text = el.text.strip()
        time.sleep(0.2)
        return text

    def present(self, by_locator, timeout=5):
        """Check if element is present (safe)."""
        try:
            wait_visible(self.driver, by_locator, timeout=timeout)
            return True
        except Exception:
            return False


