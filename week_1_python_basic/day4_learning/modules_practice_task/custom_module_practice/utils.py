# This module is created to check whether number is even or not and
# To get the current year

from datetime import datetime

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

def current_year():
    today = datetime.now().date()
    return today.year
