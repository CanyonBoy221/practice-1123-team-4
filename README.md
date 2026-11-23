# MacGuffin

A simple day counter function that utilizes 3 support functions:
* is_valid_date(year: int, month: int, day: int) -> bool: returns true if given year, month, day result in a valid date, false otherwise.
* days_in_month(year: int, month: int) -> int: returns the number of days in the given month for the given year.
* is_leap_year(year: int) -> bool: returns whether the given year is a leap year.