# utils/waits.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time, random

DEFAULT_TIMEOUT = 40

def wait_visible(driver, locator, timeout=DEFAULT_TIMEOUT):
    return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))

def wait_clickable(driver, locator, timeout=DEFAULT_TIMEOUT):
    return WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(locator))

def wait_all_visible(driver, locator, timeout=DEFAULT_TIMEOUT):
    return WebDriverWait(driver, timeout).until(EC.visibility_of_all_elements_located(locator))

def wait_url_contains(driver, fragment, timeout=DEFAULT_TIMEOUT):
    WebDriverWait(driver, timeout).until(EC.url_contains(fragment))

# ---------------- spinner/overlay handling ----------------
SPINNER_LOCATORS = [
    (By.CSS_SELECTOR, ".oxd-loading-spinner"),
    (By.CSS_SELECTOR, ".oxd-progress-bar"),
    (By.CSS_SELECTOR, ".oxd-overlay"),
    (By.CSS_SELECTOR, ".oxd-busy-overlay"),
]

def _any_spinner_displayed(driver):
    for by, sel in SPINNER_LOCATORS:
        for el in driver.find_elements(by, sel):
            try:
                if el.is_displayed():
                    return True
            except Exception:
                # Rare stale refs — ignore and continue
                pass
    return False

def wait_spinners_gone(driver, timeout=DEFAULT_TIMEOUT):
    """Wait until no known spinner/overlay is DISPLAYED. If it times out, ignore (be permissive)."""
    try:
        WebDriverWait(driver, timeout).until(lambda d: not _any_spinner_displayed(d))
    except Exception:
        # Be defensive: overlays on this site sometimes stick in DOM; continue anyway.
        pass

# ---------------- human-like pacing ----------------
def human_pause(driver, base_ms=250):
    time.sleep((base_ms + random.randint(0, 200)) / 1000.0)
