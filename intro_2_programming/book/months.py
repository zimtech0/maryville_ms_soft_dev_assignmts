# A programm to print the abbreviation of a month, given its number
# create main function
def main():
# months used as a lookup table
    months = "JanFebMarAprMayJunJulAugSepOctNovDec"   
# get user input for month    
    n = int(input("Enter a month number (1-12): "))
# compute starting position of month n in months
    pos = (n-1) * 3
# grab the appropriate slice from months
    month_abbrev = months[pos:pos + 3]
# print results
    print ("The month abbreviation is " , month_abbrev + ".")
# call main function
main() 