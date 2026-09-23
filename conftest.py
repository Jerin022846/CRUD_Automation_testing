import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="session")
def base_url():
    return os.getenv("ORANGEHRM_URL", "https://opensource-demo.orangehrmlive.com/")

@pytest.fixture(scope="session")
def creds():
    return {"username": os.getenv("ORANGEHRM_USER", "Admin"),
            "password": os.getenv("ORANGEHRM_PASS", "admin123")}

@pytest.fixture(scope="session")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    # options.add_argument("--headless=new")       # enable in CI if needed
    # options.add_argument("--no-sandbox")
    # options.add_argument("--disable-dev-shm-usage")
    d = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    d.implicitly_wait(0)
    yield d
    d.quit()

@pytest.fixture(scope="session")
def login_once(driver, base_url, creds):
    """Log in once for the whole test session."""
    from pages.login_page import LoginPage
    # If already on dashboard (cached session), do nothing
    if "/dashboard" not in driver.current_url:
        LoginPage(driver).open(base_url).login(creds["username"], creds["password"])
    assert "/dashboard" in driver.current_url
    return driver
