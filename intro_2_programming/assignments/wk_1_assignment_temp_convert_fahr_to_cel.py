#Simple program to take user input, current temperature in celsius, 
# convert the input into fahrenheit and output the results to the results
#to the screen

def main():
    # Repeat loop for 3 user Celsius inputs
    for temp_conversions in range(3):
    #Get input from user
        fahrenheit = float(input("Enter the current temperature in farenheit degrees: "))
    #covert fahrenheit to celsius 
        celsius= 5/9 * (fahrenheit - 32)
    #output results to screen
        print("The current temperature in celsius degrees is: ",celsius)
# call the function
main()