class WeekDay:

    def get_sunday(self):
        return "Sunday"
    
    def get_monday(self):
        return "Monday"

    def get_tuesday(self):
        return "Tuesday"
    
    def get_wednesday(self):
        return "Wednesday"

    def get_thursday(self):
        return "Thursday"
    
    def get_friday(self):
        return "Friday"

    def get_saturday(self):
        return "Saturday"

    def default(self):
        return "Invalid day number"

    
    def get_week_day(self, day_number):
        days = {
            1: self.get_sunday,
            2: self.get_monday,
            3: self.get_tuesday,
            4: self.get_wednesday,
            5: self.get_thursday,
            6: self.get_friday,
            7: self.get_saturday
        }
        return days.get(day_number, self.default)()

try:
    day_number = int(input("Enter day number: "))
    week_day = WeekDay()
    day = week_day.get_week_day(day_number)
    if (day != "Invalid day number"):
        print("Day", day_number, "of the week is", end=" ")
    print(day)
except ValueError:
    print("Value should be integer")