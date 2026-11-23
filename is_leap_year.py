def is_leap_year(year: int) -> bool: # This looks sick!
    if year % 400 == 0: # Years divisible by 400 are leap years.
        return True
    if year % 100 == 0: # Other years that are divisible by 100 are usually not leap years.
        return False
    return year % 4 == 0 # Usually, years divisible by 4 are leap years.