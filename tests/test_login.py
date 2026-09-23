from pages.login_page import LoginPage
from utils.waits import wait_url_contains


def test_login(login_once):
    driver = login_once
    assert "/index" in driver.current_url
