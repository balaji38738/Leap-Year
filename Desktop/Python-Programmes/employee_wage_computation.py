import random

print("Welcome to employee wage computation")

#constants
IS_FULL_TIME = 1
IS_PART_TIME = 2
EMP_RATE_PER_HOUR = 200
NUM_WORKING_DAYS = 20

#variables
emp_wage = total_emp_wage = emp_hours = 0

#Loop to iterate over working days in month
for day in range(0, NUM_WORKING_DAYS):
    emp_presence = random.randint(0, 3)
    if emp_presence == IS_FULL_TIME:
        emp_hours = 8
    elif emp_presence == IS_PART_TIME:
        emp_hours = 4
    emp_wage = emp_hours * EMP_RATE_PER_HOUR
    total_emp_wage += emp_wage
print("Total employee wage for month:", total_emp_wage)