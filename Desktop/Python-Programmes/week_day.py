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
        return "Incorrect day"

    days = {
        1: get_sunday,
        2: get_monday,
        3: get_tuesday,
        4: get_wednesday,
        5: get_thursday,
        6: get_friday,
        7: get_saturday
    }
    
    def get_week_day(self, day_number):
        return WeekDay.days.get(day_number, self.default())(self)

week_day = WeekDay()
day = week_day.get_week_day(3)
print(day)