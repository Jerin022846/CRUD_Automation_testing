"""
Tiny state helper so tests can share the created employee id/name.
We keep it file-based to be dead simple and runner-agnostic.
"""
import json
from pathlib import Path

STATE_FILE = Path(".state_emp.json")

def save_emp(emp):
    STATE_FILE.write_text(json.dumps(emp, indent=2))

def load_emp():
    if not STATE_FILE.exists():
        raise RuntimeError("No saved employee state. Run 02_test_add_employee.py first.")
    return json.loads(STATE_FILE.read_text())

