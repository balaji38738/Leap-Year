import random

print("Welcome to employee wage computation")

class EmployeeWageComputation:
        #constants
        __IS_FULL_TIME = 1
        __IS_PART_TIME = 2

        def __init__(
                self, emp_rate_per_hour,
                num_working_days, max_hours_in_month):
            self.__EMP_RATE_PER_HOUR = emp_rate_per_hour
            self.__NUM_WORKING_DAYS = num_working_days
            self.__MAX_HOURS_IN_MONTH = max_hours_in_month
            self.__total_emp_wage = 0

        @staticmethod
        def compute_emp_wage(company):

            #variables
            emp_hours = total_emp_hours = 0
            total_working_days = emp_wage = 0

            #Loop to iterate over working days in month
            while (total_working_days < company.__NUM_WORKING_DAYS
                        and total_emp_hours < company.__MAX_HOURS_IN_MONTH):
                emp_presence = random.randint(0, 3)
                if emp_presence == __class__.__IS_FULL_TIME:
                    emp_hours = 8
                elif emp_presence == __class__.__IS_PART_TIME:
                    emp_hours = 4
                emp_wage = emp_hours * company.__EMP_RATE_PER_HOUR
                company.__total_emp_wage += emp_wage
                total_working_days += 1
                total_emp_hours += emp_hours
                print("Day", total_working_days, " | Employee hours: ", emp_hours,
                        " | Employee wage: ", emp_wage)
            print("Total employee wage for month:", company.__total_emp_wage)

emp_wage_computation1 = EmployeeWageComputation(200, 20, 120)
emp_wage_computation2 = EmployeeWageComputation(300, 25, 110)
print("Employee wage of first company")
EmployeeWageComputation.compute_emp_wage(emp_wage_computation1)
print("\nEmployee wage of second company")
EmployeeWageComputation.compute_emp_wage(emp_wage_computation2)