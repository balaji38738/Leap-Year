import random

print("Welcome to employee wage computation")

class EmployeeWageComputation:
        #constants
        IS_FULL_TIME = 1
        IS_PART_TIME = 2
        EMP_RATE_PER_HOUR = 200
        NUM_WORKING_DAYS = 20
        MAX_HOURS_IN_MONTH = 120

        #variables
        emp_wage = total_emp_wage = 0
        emp_hours = total_emp_hours = total_working_days = 0

        @staticmethod
        def compute_emp_wage():
            #Loop to iterate over working days in month
            while (__class__.total_working_days < __class__.NUM_WORKING_DAYS
                        and __class__.total_emp_hours < __class__.MAX_HOURS_IN_MONTH):
                emp_presence = random.randint(0, 3)
                if emp_presence == __class__.IS_FULL_TIME:
                    __class__.emp_hours = 8
                elif emp_presence == __class__.IS_PART_TIME:
                    __class__.emp_hours = 4
                __class__.emp_wage = __class__.emp_hours * __class__.EMP_RATE_PER_HOUR
                __class__.total_emp_wage += __class__.emp_wage
                __class__.total_working_days += 1
                __class__.total_emp_hours += __class__.emp_hours
                print("Day", __class__.total_working_days, " | Employee hours: ", __class__.emp_hours,
                        " | Employee wage: ", __class__.emp_wage)
            print("Total employee wage for month:", __class__.total_emp_wage)

EmployeeWageComputation.compute_emp_wage()