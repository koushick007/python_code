
# Date to Day

date=int(input("Enter the date : "))
month=int(input("Enter the month : "))
year=int(input("Enter the year : "))
list_month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
list_weekdays = ['Sunday','Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
list_end_date= [31,28,31,30,31,30,31,31,30,31,30,31]
list_end_leap_date = [31,29,31,30,31,30,31,31,30,31,30,31]
list_date = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
list_date2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
list_date_leap = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
list_date4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
month_days = 0

# Calculating year
initial_year = year-1
initial_month = 12
initial_date = 31

if date <= 31 and month <= 12:
    cal_leap_year = initial_year / 4
    normal_year = initial_year - cal_leap_year
    year_in_days = (cal_leap_year * 366) + (normal_year * 365)

    # Calculating months
    if year % 4 == 0:
        for i in range(0, month - 1):
            month_days = month_days + list_end_leap_date[i]
    else:
        for i in range(0, month - 1):
            month_days = month_days + list_end_date[i]

    # Calculating days
    final_days = month_days + date + year_in_days

    # Calculating date to days
    final = int(final_days % 7)
    print(str(list_weekdays[final - 1]))
else:
    print("Wrong input! Please check your date and month again")


