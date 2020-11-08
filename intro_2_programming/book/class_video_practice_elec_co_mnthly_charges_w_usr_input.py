#create a program to calculate monthly electric charges based on user input for on peak/off peak hrs used
def electric_company_monthly_charges():
#create variable to calculate on Peak hrs based on usr input
    total_on_peak_hrs_usr_input= float(input("Please enter total on peak hrs used for the month:  "))
#create variable to calculate off Peak hrs based on usr input
    total_off_peak_hrs_usr_input= float(input("Please enter total off peak hrs used for the month:  "))
#create variable for total on peak hrs charges in cents
    total_on_peak_hrs_charges_in_cents =  total_on_peak_hrs_usr_input * 31.5
#create variable for total off peak hrs charges in cents
    total_off_peak_hrs_charges_in_cents= total_off_peak_hrs_usr_input * 7.4
#create variable to calculate total cost in cents
    total_charges_in_cents = total_on_peak_hrs_charges_in_cents + total_off_peak_hrs_charges_in_cents
#create variable to converst total cost in cents to dollars
    total_charges_dollars =  total_charges_in_cents / 100
#print results of total cost in dollars
    print(total_charges_dollars)
electric_company_monthly_charges()