# create a note encoding program
# create the main function
def main():
# Program introduction
    print('This program converts a textual message into a sequence')
    print('of numbers representing the Unicode encoding of the message.\n')
# get the message to encode
    message = input('Please enter the message you would like to encode: ')
#   print the letter number of the character
    print('\nHere are the Unicode codes: ')
# for each character in the message
    for ch in message: 
# convert each character to a number
        print(ord(ch), end =' ')

#print blank lines before prompt
print()

# call the main function
main()