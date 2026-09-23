# OrangeHRM Demo – Selenium Python CRUD Automation

End-to-end CRUD automation for the OrangeHRM demo (PIM module) using Selenium + Pytest.

## What this suite covers

1. **Login**
2. **Create** Employee (PIM → Add Employee)
3. **Update** Personal Details + Job + Salary
4. **Read** (Search by Employee ID)
5. **Delete** (Row-level delete with confirmation modal)

Each step includes assertions (toasts, URL, header text, table counts, etc).

---

## Prerequisites

- **Python 3.10+**
- **Google Chrome** (latest)
- Internet access (to download the matching chromedriver automatically)
- (Optional) Virtualenv installed

> Credentials default to `Admin / admin123` and URL `https://opensource-demo.orangehrmlive.com/`.  
> You can override them via environment variables:
> - `ORANGEHRM_URL`
> - `ORANGEHRM_USER`
> - `ORANGEHRM_PASS`

---

## Setup

```bash
# 1) Clone or copy this folder
cd orangehrm-automation

# 2) (Optional) Create & activate a virtual environment
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# 3) Install dependencies
pip install -r requirements.txt

