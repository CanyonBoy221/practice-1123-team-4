from days_in_month import days_in_month

def is_valid_date(year: int, month: int, day: int) -> bool:
    max_days = days_in_month(year, month)
    if month > 12: return False
    if day > max_days: return False
    return True