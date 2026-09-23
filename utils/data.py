from datetime import datetime

def unique_suffix():
    return datetime.now().strftime("%Y%m%d_%H%M%S")

def unique_numeric(n=4):
    return unique_suffix()[-n:]

