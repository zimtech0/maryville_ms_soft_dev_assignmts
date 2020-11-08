# Create a program to calculate 10 year future value of an investment 
# based on annual apr

def main():
#Print introduction to user
    print("This program calculates the future value")
    print("of a 10 year investment")
#Get user input for initial principle
    principle = eval(input("Please enter the initial principle : "))
    interest = eval(input("Please enter the interest rate in two decimal format,eg .03 : "))
#Create loop to calculate 10 years of interest
    for i in range(10):
        principle = principle *(1 + interest)
#Output results to the screen        
    print("Based on the information you provided, your account will have a value of :",principle," in 10 years")

#Call function
main()

