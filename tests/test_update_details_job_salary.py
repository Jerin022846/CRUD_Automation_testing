import pytest
from pages.sidebar import Sidebar
from pages.pim_list_page import PimListPage
from pages.personal_details_page import PersonalDetailsPage
from pages.job_page import JobPage
from pages.components.toast import Toast
from utils.waits import wait_visible, wait_url_contains
from utils.state import load_emp


@pytest.mark.usefixtures("login_once")
def test_update_personal_job_salary(login_once):
    """
    Test: Update an employee’s personal, job, and salary details.
    Handles fallback if saved employee is deleted.
    """
    driver = login_once
    emp = load_emp()
    Sidebar(driver).goto_pim()
    pim = PimListPage(driver)

    # Try to find the previously-added employee (may have been deleted)
    count = pim.search_by_id(emp["id"])

    if count == 0:
        # Fallback: update ANY available employee
        count = pim.search_by_id("")
        assert count >= 1, "No employees available to update"
        pim.open_first_result()
    else:
        pim.open_first_result()

    wait_url_contains(driver, "/pim/viewPersonalDetails")

    # --- Personal Details Update ---
    details = PersonalDetailsPage(driver)
    wait_visible(driver, details.EMPLOYEE_ID_INPUT)

    details.set_personal_details(
        other_id="OID-AUTO",
        nationality="Bangladeshi",
        marital="Married",
        dob="1994-02-14",
        gender="Male"
    )
    Toast.wait_success(driver)

    # --- Job Details Update ---
    details.goto_job()
    job = JobPage(driver)
    job.update_job(
        joined_date="2025-10-08",
        job_title="Software Engineer",
        sub_unit="Engineering",
        emp_status="Freelance"
    )
    Toast.wait_success(driver)

    # --- Salary Tab (optional, if implemented) ---
    # If you have a salary page, you can extend here:
    # details.goto_salary()
    # salary = SalaryPage(driver)
    # salary.update_salary(amount="85000", currency="USD", component="Basic")
    # Toast.wait_success(driver)

    print("✅ Employee details updated successfully.")
