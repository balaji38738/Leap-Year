import random

print("Welcome to employee wage computation")

#constants
IS_FULL_TIME = 1
IS_PART_TIME = 0
EMP_RATE_PER_HOUR = 200

#variables
emp_hours, emp_wage = 0, 0

emp_presence = random.randint(0, 3)
if emp_presence == IS_FULL_TIME:
    emp_hours = 8
elif emp_presence == IS_PART_TIME:
    emp_hours = 4
emp_wage = emp_hours * EMP_RATE_PER_HOUR
print("Employee wage:", emp_wage)