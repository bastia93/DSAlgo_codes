from datetime import date


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day


def calculate_age(dob):
    final_date = Date(year=2022, month=8, day=1)
    ans_day = 0
    ans_month = 0
    ans_year = 0
    if dob.day > final_date.day:
        final_date.day += 31
        final_date.month -= 1

    ans_day = final_date.day - dob.day

    if dob.month > final_date.month:
        final_date.month += 12
        final_date.year -= 1
    ans_month = final_date.month - dob.month

    ans_year = final_date.year - dob.year

    return [ans_year, ans_month, ans_day]


date_str = input("Enter the date of birth (Ex 17 4 2004): ")
while date_str != 'q':
    date_arr = date_str.strip().split()
    date_arr = [int(i) for i in date_arr]

    if date_arr[2] > 1900:
        dob = Date(date_arr[2], date_arr[1], date_arr[0])
        age = calculate_age(dob)
        if date_arr[2] == 2004 and date_arr[1] == 2:
            age[2] += 1

        print(f"{age[0]} years, {age[1]} months, {age[2]} days")
    else:
        print("Enter in correct order.")

    date_str = input("Enter the date of birth (Ex 17 4 2004): ")




