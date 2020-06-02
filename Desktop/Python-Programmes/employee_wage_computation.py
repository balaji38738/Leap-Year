import random

print("Welcome to employee wage computation")

def compute_emp_wage():
    #constants
    IS_FULL_TIME = 1
    IS_PART_TIME = 2
    EMP_RATE_PER_HOUR = 200
    NUM_WORKING_DAYS = 20
    MAX_HOURS_IN_MONTH = 120

    #variables
    emp_wage = total_emp_wage = 0
    emp_hours = total_emp_hours = total_working_days = 0

    #Loop to iterate over working days in month
    while (total_working_days < NUM_WORKING_DAYS
                and total_emp_hours < MAX_HOURS_IN_MONTH):
        emp_presence = random.randint(0, 3)
        if emp_presence == IS_FULL_TIME:
            emp_hours = 8
        elif emp_presence == IS_PART_TIME:
            emp_hours = 4
        emp_wage = emp_hours * EMP_RATE_PER_HOUR
        total_emp_wage += emp_wage
        total_working_days += 1
        total_emp_hours += emp_hours
        print("Day", total_working_days, " | Employee hours: ", emp_hours,
                " | Employee wage: ", emp_wage)
    print("Total employee wage for month:", total_emp_wage)

compute_emp_wage()