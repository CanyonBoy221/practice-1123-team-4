<<<<<<< HEAD
import sys
import is_valid_date
from days_in_month import days_in_month

def day_counter(year1: int, month1: int, day1: int, year2: int, month2: int, day2: int) -> int:
    day_count = 0
=======
import is_valid_date

def day_counter(year1: int, month1: int, day1: int, year2: int, month2: int, day2: int) -> int:
    day_count = 0

>>>>>>> 95f82598d2f11fb7c879ada15f52a278efc6b6c7
    current_year = year1
    current_month = month1
    current_day = day1

<<<<<<< HEAD
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
=======
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
>>>>>>> 95f82598d2f11fb7c879ada15f52a278efc6b6c7
