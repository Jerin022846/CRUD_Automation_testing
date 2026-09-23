from pages.sidebar import Sidebar
from pages.pim_list_page import PimListPage
from pages.add_employee_page import AddEmployeePage
from pages.personal_details_page import PersonalDetailsPage
from pages.components.toast import Toast
from utils.state import save_emp
from utils.waits import wait_url_contains,human_pause, wait_visible
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.data import unique_numeric

def test_add_employee(login_once):
    driver = login_once

    # PIM → Add
    Sidebar(driver).goto_pim()
    pim = PimListPage(driver)
    pim.add_employee()

    # Fill only names (auto Employee Id)
    add = AddEmployeePage(driver)
    first, middle, last = "Ashikur", "Rahman", "Khan"
    add.fill(first, middle, last)
    human_pause(driver,300)
    add.save()
    dup_msg = (By.XPATH, "//span[contains(@class,'oxd-input-field-error-message') and contains(.,'already exists')]"
                    "| //span[contains(.,'Employee Id already exists')]")
    if BasePage(driver).present(dup_msg, timeout=2):
        new_id = "9" + unique_numeric(4)
        driver.find_element(*add.EMPLOYEE_ID_INPUT).clear()
        driver.find_element(*add.EMPLOYEE_ID_INPUT).send_keys(new_id)
        add.save()
    # Toast and navigation
    Toast.wait_success(driver)
    wait_url_contains(driver, "/pim/viewPersonalDetails")

    details = PersonalDetailsPage(driver)

    # Ensure the Personal Details form is loaded (Employee Id field visible)
    wait_visible(driver, details.EMPLOYEE_ID_INPUT)
    emp_id = details.get_employee_id().strip()
    assert emp_id, "Employee Id should be present after save"


    # Save the real generated ID for the next tests
 
    save_emp({"first": first, "middle": middle, "last": last, "id": emp_id}) 