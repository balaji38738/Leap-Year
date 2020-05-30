def check_leap_year():
    year = int(input("Enter year "))
    if year < 1000 and year > 9999:
        print("Invalid input")
    else:
        if year % 400 == 0:
            print("Leap year")
        elif (year % 4 == 0) and (year % 100 != 0):
            print("Leap year")
        else:
            print("Not a leap year")


check_leap_year()