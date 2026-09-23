# CRUD_Automation_testing

End-to-end CRUD test automation for the OrangeHRM demo application (PIM module), implemented with Selenium and Pytest.

## What this test suite includes

1. **User Login**
2. **Create** an Employee (PIM → Add Employee)
3. **Update** Personal Information + Job Details + Salary
4. **Read** employee records (Search using Employee ID)
5. **Delete** an Employee (Delete directly from the row with confirmation)

Every operation contains relevant validations, including toast notifications, URL verification, page/header text, employee table counts, and other assertions.

---

## Prerequisites

* **Python 3.10 or newer**
* **Google Chrome** (up to date)
* Internet connection (required for automatic download of the compatible ChromeDriver)
* (Optional) Virtual environment support

> The default login credentials are `Admin / admin123`, and the application URL is `https://opensource-demo.orangehrmlive.com/`.
> These values can be customized through the following environment variables:
>
> * `ORANGEHRM_URL`
> * `ORANGEHRM_USER`
> * `ORANGEHRM_PASS`

---

## Setup

```bash
# 1) Navigate to the project directory
cd orangehrm-automation

# 2) (Optional) Set up and activate a virtual environment
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# 3) Install the required packages
pip install -r requirements.txt
```
