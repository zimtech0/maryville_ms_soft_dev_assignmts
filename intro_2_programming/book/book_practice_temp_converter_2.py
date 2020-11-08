#algorithm:
# Input the temperature in degrees Celsius (call it celsius)
# Calculate fahrenheit as 9/5 celsius + 32
# Output fahrenheit
# if fahrenheit > 90
#   print a heat warning
# if fahrenheit < 30
#   print a cold warning

#Simple program to take user input, current temperature in celsius, 
# convert the input into fahrenheit and output the results to the results
#to the screen

# create main function
def main():
    #Get input from user
        celsius = float(input("Enter the current temperature in celsius degrees: "))
    #covert celsius to fahrenheit
        fahrenheit =9/5 * celsius + 32 
    #output results to screen
        print("The current temperature in fahrenheit degrees is: ",fahrenheit)

# create conditons for heat and cold warnings: one way or simple decision control
        if fahrenheit > 90:
            print("It's really hot out there. Be careful!")
        if fahrenheit < 30:
            print('Brrrrr. Be sure to dress warmly!')

# call the function
main()