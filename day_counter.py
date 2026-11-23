import is_valid_date

def day_counter(year1: int, month1: int, day1: int, year2: int, month2: int, day2: int) -> int:
    day_count = 0

    current_year = year1
    current_month = month1
    current_day = day1

    while not (current_year == year2 and current_month == month2 and current_day == day2):
        day_count += 1

        current_day += 1
        if not is_valid_date.is_valid_date(current_year, current_month, current_day):
            current_day += 1
            current_month += 1

            if not is_valid_date.is_valid_date(current_year, current_month, current_day):
                current_month = 1
                current_year = 1


    return day_count