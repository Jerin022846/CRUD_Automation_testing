import pytest
from pages.sidebar import Sidebar
from pages.pim_list_page import PimListPage
from pages.components.delete_modal import DeleteModal
from pages.components.toast import Toast
from utils.state import load_emp

def test_delete_employee_row_level(login_once):
    driver = login_once
    emp = load_emp()

    Sidebar(driver).goto_pim()
    pim = PimListPage(driver)
    count = pim.search_by_id(emp["id"])
    assert count >= 1, f"No rows found for Employee ID {emp['id']} (already deleted?)"

    pim.delete_first_result()
    DeleteModal.confirm(driver)
    Toast.wait_success(driver)

    # verify gone
    count2 = pim.search_by_id(emp["id"])
    assert count2 == 0
