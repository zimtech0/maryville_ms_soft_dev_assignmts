# a program to print the month abbreviation, given its number.

# create a main function
def main():
# create a list of months
    months = ['Jan','Feb','Mar','Apr','May','Jun','Jul'
              ,'Aug','Sep','Oct','Nov','Dec']
# get user input in a number
    n = int(input("Enter a month number (1-12): "))    
#print output
    print('The month abbreviation is', months[n-1] + '.')
# call the main function
main()