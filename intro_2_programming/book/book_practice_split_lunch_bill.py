# a program to split lunch bill
def lunch_bill_split():
#total bill cost of $40
    total_bill_cost = 40
 #number of people to split bill
    number_of_people = 4
 #calculate tip
    tip_amount = .20
#calculate cost per person
    cost_per_person = ((total_bill_cost + (total_bill_cost * tip_amount))/number_of_people)
#print cost per person to screen
    print(cost_per_person)


lunch_bill_split()
