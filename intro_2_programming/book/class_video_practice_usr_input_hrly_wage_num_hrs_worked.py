# Create a program to allow users to input their hourly wage and number of hrs worked per week to calculate weekly pay
def employee_gross_pay():
# variable to hold usr hrly wage input
    usr_hrly_wage_input = float(input("Please enter you hourly pay rate:  "))
# variable to hold usr hrs worked per week input
    usr_hrs_weekly_hrs_worked= float(input("Please enter the total weekly hours worked:  "))
# variable to hold weekly gross pay total
    weekly_gross_pay= usr_hrly_wage_input * usr_hrs_weekly_hrs_worked
# print weekly gross
    print(weekly_gross_pay)
employee_gross_pay()