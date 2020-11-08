# a simple program to decode an encoded message
# create main function
def main():
# introduction to program
    print('This program converts a sequence of Unicode numbers into')
    print('the string of text that it represents.\n')
# get the message from user
    in_string = input('Please enter the Unicode-encoded message: ')
# Loop through each substring and build Unicode Message
    message = ""
    for number_String in in_string.split():
# convert digits to a number
        code_number = int(number_String)
# concatenate character to message
        message = message + chr(code_number)
# print output
    print('\nThe decoded message is:', message)
# call main function
main()