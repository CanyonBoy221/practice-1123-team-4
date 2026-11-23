import sys
import is_valid_date
from days_in_month import days_in_month

def day_counter(year1: int, month1: int, day1: int, year2: int, month2: int, day2: int) -> int:
    day_count = 0
    current_year = year1
    current_month = month1
    current_day = day1

    while (current_year, current_month, current_day) != (year2, month2, day2):
        day_count += 1
        current_day += 1

        if current_day > days_in_month(current_year, current_month):
            current_day = 1
            current_month += 1

            if current_month > 12:
                current_month = 1
                current_year += 1

    return day_count


if __name__ == "__main__":
    if len(sys.argv) == 7:
        y1 = int(sys.argv[1])
        m1 = int(sys.argv[2])
        d1 = int(sys.argv[3])
        y2 = int(sys.argv[4])
        m2 = int(sys.argv[5])
        d2 = int(sys.argv[6])

        print(f"The number of days between those dates is {day_counter(y1, m1, d1, y2, m2, d2)}")
    else:
        print("Please supply 6 arguments in this format: yr1, m1, d1, yr2, m2, d2")