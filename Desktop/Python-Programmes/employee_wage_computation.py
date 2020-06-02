import random

print("Welcome to employee wage computation")

#constants
IS_FULL_TIME = 1

emp_presence = random.randint(0, 1)
if emp_presence == IS_FULL_TIME:
    print("Employee is present")
else:
    print("Employess is absent")