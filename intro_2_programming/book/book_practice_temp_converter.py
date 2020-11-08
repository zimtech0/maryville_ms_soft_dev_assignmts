#Simple program to take user input, current temperature in celsius, 
# convert the input into fahrenheit and output the results to the results
#to the screen

def main():
    # Repeat loop for 3 user Celsius inputs
    for temp_conversions in range(3):
    #Get input from user
        celsius = float(input("Enter the current temperature in celsius degrees: "))
    #covert celsius to fahrenheit
        fahrenheit =9/5 * celsius + 32 
    #output results to screen
        print("The current temperature in fahrenheit degrees is: ",fahrenheit)
# call the function
main()