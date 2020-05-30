def check_leap_year(year):
    if year < 1000 or year > 9999:
        print("Year should be in range 1000-9999")
    else:
        if ((year % 400 == 0)
            or ((year % 4 == 0) and (year % 100 != 0))):
                print("Leap year")
        else:
            print("Not a leap year")


try:
    year = int(input("Enter year "))
    check_leap_year(year)
except ValueError:
    print("Invalid value")