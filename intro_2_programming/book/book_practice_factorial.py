# Program to compute the factorial of a number
# Illustrate for loop with an accumulator



def main():
    # Get user input
    n = int(input("Please enter a whole number: "))
    #Process user input
    #create variable to hold computational results
    fact = 1
    #create loop to go through range based on int given by user
    for factor in range(n,1,-1):
    #expression to compute results    
        fact = fact * factor
    #Output results to screen    
    print("The factorial of", n, "is", fact)

main()