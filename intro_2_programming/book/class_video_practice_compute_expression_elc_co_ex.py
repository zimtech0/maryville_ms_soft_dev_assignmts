# compute electric company charges
#def electric_company_charges():
# compute peak/off hr usage charges
    #charges=(((31.6*120)+(7.4*80))/100)
# print results
 #   print(charges)
#electric_company_charges()

#compute electric company charges for better readability/reuseability
def electric_company_charges():
#company on peak hrs charges in cents
    on_peak_hrs_charges_in_cents = 31.5*120
#company off peak hrs charges in cents
    off_peak_hrs_charges_in_cents =7.4*80
# total charges converted to $$
    total_charges= (on_peak_hrs_charges_in_cents + off_peak_hrs_charges_in_cents)/100
#print results
    print(total_charges)

electric_company_charges()