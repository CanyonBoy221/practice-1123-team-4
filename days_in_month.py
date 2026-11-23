import is_leap_year

def days_in_month(year: int, month: int) -> int:
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    if month in [4, 6, 9, 11]:
        return 30
    if month == 2:
        if is_leap_year.is_leap_year(year):
            return 29
        return 28
    return 0