import random
from abc import ABC, abstractclassmethod

print("Welcome to employee wage computation")

class InvalidInputError(Exception):
    def __init__(self, message = "Input should be (y/n)"):
        self.message = message
        super().__init__(self.message)


class Computable(ABC):
    @abstractclassmethod
    def compute_emp_wage(cls):
        pass

    @abstractclassmethod
    def display_daily_wage(cls):
        pass

    @abstractclassmethod
    def add_employees(cls):
        pass

    @abstractclassmethod
    def get_total_emp_wage(cls):
        pass


class EmployeeWageComputation(Computable):
        employee_list = []

        @classmethod
        def compute_emp_wage(cls):

            #constants
            IS_FULL_TIME = 1
            IS_PART_TIME = 2

            for employee in cls.employee_list:
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
                    if emp_presence == IS_FULL_TIME:
                        emp_hours = 8
                    elif emp_presence == IS_PART_TIME:
                        emp_hours = 4
                    emp_wage = emp_hours * EMP_RATE_PER_HOUR
                    employee.add_daily_wage(emp_wage)
                    total_emp_wage += emp_wage
                    total_working_days += 1
                    total_emp_hours += emp_hours
                employee.set_total_emp_wage(total_emp_wage)
        
        @classmethod
        def display_employee_wage(cls):
            employee_no = 0
            for employee in cls.employee_list:
                employee_no += 1
                print("\nEmployee wage of employee", employee_no)
                daily_wage = employee.get_daily_wage()
                for day in range(0, len(daily_wage)):
                    print("day", day, ":" , daily_wage[day])
                print("Employee monthly wage", employee.get_total_emp_wage())

        @classmethod
        def add_employees(cls):
            user_input = "y"
            while user_input == "y":
                #Generate Employee rate between 100 to 300
                emp_rate_per_hour = random.randint(100, 300)

                #Generate Employee working days between 20 to 25
                num_working_days = random.randint(20, 25)

                #Generate Employee work hours between 100 to 150
                max_hours_in_month = random.randint(100, 150)
                
                company_employee = CompanyEmployee(emp_rate_per_hour, num_working_days,
                                                    max_hours_in_month)
                cls.employee_list.append(company_employee)
                user_input = input("Employee added, do you want to add more ?(y/n): ")
                if user_input not in ["y", "n"]:
                    raise InvalidInputError()

        @classmethod
        def get_total_emp_wage(cls):
            #Get the total employee wage when queried by the user
            try:
                employee_no = int(input("Enter employee number to get total wage: ")) 
                if employee_no > 0 and employee_no <= len(__class__.employee_list):
                    print("\nTotal wage of employee", employee_no, end=": ")
                    print(cls.employee_list[employee_no - 1].get_total_emp_wage())
                else:
                    print("Employee not found")
            except ValueError:
                print("Employee number should be integer")


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

EmployeeWageComputation.add_employees()
EmployeeWageComputation.compute_emp_wage()
EmployeeWageComputation.display_employee_wage()
EmployeeWageComputation.get_total_emp_wage()