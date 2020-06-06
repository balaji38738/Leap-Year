class Time:
    def __init__(self, hour, minute, sec):
        self.__hour = hour + (sec // 60 + minute) // 60

        #Minutes can't be >= 60 in standard representation
        self.__minute = (sec // 60 + minute) % 60

        #Seconds can't be >= 60 in standard representation
        self.__sec = sec % 60

    def __repr__(self):
        return f"{self.__hour}:{self.__minute:02d}:{self.__sec:02d}"

    def __add__(self, time):
        total_time_sec = ((self.__hour + time.__hour) * 3600
                            + (self.__minute + time.__minute) * 60
                            + self.__sec + time.__sec)
        total_hours = total_time_sec // 3600
        total_minutes = total_time_sec % 3600 // 60
        total_sec = total_time_sec % 60
        return Time(total_hours, total_minutes, total_sec)
    
time1 = Time(12, 13, 13)
time2 = Time(13, 54, 55)
print(time1 + time2)