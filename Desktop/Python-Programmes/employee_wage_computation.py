import random
from abc import ABC, abstractmethod

print("Welcome to employee wage computation")

class InvalidInputError(Exception):
    def __init__(self, message = "Input should be (y/n)"):
        self.message = message
        super().__init__(self.message)


class Computable(ABC):
    @abstractmethod
    def compute_emp_wage(self, employee):
        pass

    @abstractmethod
    def display_daily_wage(
            self, total_working_days,
            emp_hours, emp_wage):
        pass


class EmployeeWageComputation(Computable):
        #constants
        __IS_FULL_TIME = 1
        __IS_PART_TIME = 2

        @staticmethod
        def compute_emp_wage(employee_list):
            company_no = 0
            for employee in employee_list:
                company_no += 1
                MAX_HOURS_IN_MONTH = employee.get_max_hours_in_month()
                NUM_WORKING_DAYS = employee.get_num_working_days()
                EMP_RATE_PER_HOUR = employee.get_emp_rate_per_hour()

                #variables
                emp_hours = total_emp_hours = 0
                total_working_days = emp_wage = 0
                total_emp_wage = 0

                #Loop to iterate over working days in month
                while (total_working_days < NUM_WORKING_DAYS
                            and total_emp_hours < MAX_HOURS_IN_MONTH):
                    emp_presence = random.randint(0, 3)
                    if emp_presence == __class__.__IS_FULL_TIME:
                        emp_hours = 8
                    elif emp_presence == __class__.__IS_PART_TIME:
                        emp_hours = 4
                    emp_wage = emp_hours * EMP_RATE_PER_HOUR
                    employee.add_daily_wage(emp_wage)
                    total_emp_wage += emp_wage
                    total_working_days += 1
                    total_emp_hours += emp_hours
                employee.set_total_emp_wage(total_emp_wage)
        
        @staticmethod
        def display_employee_wage(employee_list):
            employee_no = 0
            for employee in employee_list:
                employee_no += 1
                print("\nEmployee wage of employee", employee_no)
                daily_wage = employee.get_daily_wage()
                for day in range(0, len(daily_wage)):
                    print("day", day, ":" , daily_wage[day])
                print("Employee monthly wage", employee.get_total_emp_wage())


class CompanyEmployee:
    def __init__(
            self, emp_rate_per_hour,
            num_working_days, max_hours_in_month):
        self.__EMP_RATE_PER_HOUR = emp_rate_per_hour
        self.__NUM_WORKING_DAYS = num_working_days
        self.__MAX_HOURS_IN_MONTH = max_hours_in_month
        self.__total_emp_wage = 0
        self.__daily_wages = []

    def get_emp_rate_per_hour(self):
        return self.__EMP_RATE_PER_HOUR

    def get_num_working_days(self):
        return self.__NUM_WORKING_DAYS
    
    def get_max_hours_in_month(self):
        return self.__MAX_HOURS_IN_MONTH

    def get_total_emp_wage(self):
        return self.__total_emp_wage

    def set_total_emp_wage(self, total_emp_wage):
        self.__total_emp_wage = total_emp_wage

    def add_daily_wage(self, wage):
        self.__daily_wages.append(wage)
    
    def get_daily_wage(self):
        return self.__daily_wages


user_input = "y"
employee_list = []
while user_input == "y":
    #Generate Employee rate between 100 to 300
    emp_rate_per_hour = random.randint(100, 300)

    #Generate Employee working days between 20 to 25
    num_working_days = random.randint(20, 25)

    #Generate Employee work hours between 100 to 150
    max_hours_in_month = random.randint(100, 150)
    
    company_employee = CompanyEmployee(emp_rate_per_hour, num_working_days,
                                        max_hours_in_month)
    employee_list.append(company_employee)
    user_input = input("Employee added, do you want to add more ?(y/n): ")
    if user_input not in ["y", "n"]:
        raise InvalidInputError()

EmployeeWageComputation.compute_emp_wage(employee_list)
EmployeeWageComputation.display_employee_wage(employee_list)
