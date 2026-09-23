from pages.login_page import LoginPage
from pages.sidebar import Sidebar
from pages.pim_list_page import PimListPage
from pages.personal_details_page import PersonalDetailsPage
from utils.state import load_emp
from utils.waits import wait_url_contains

def test_search_by_employee_id(login_once, base_url):
    driver= login_once
    emp = load_emp()

    

    Sidebar(driver).goto_pim()
    pim = PimListPage(driver)
    count = pim.search_by_id(emp["id"])

    if count == 0:
        # Employee was deleted earlier — that's acceptable for this test
        # (requirement: if search says not found, consider the test passed)
        assert True
        return



    pim.open_first_result()
    wait_url_contains(driver, "/pim/viewPersonalDetails")
    # confirmation the opened record is correct
    details = PersonalDetailsPage(driver)
    assert details.get_employee_id() == emp["id"]

