# a program to convert a sequence of Unicode numbers into a
# string of text. Efficient version using list accumulator

def main():
    print('This program converts a sequence of Unicode numbers into')
    print('the string of text that it represents.\n')

# get the message to encode
    in_string = input('Please enter the Unicode-encoded message: ')

# Loop through each substring and build Unicode message
    chars = []
    for number_string in in_string.split():
# convert digits to a number
        code_name = int(number_string)
# accumulate new character
        chars.append(chr(code_name))
    message = ''.join(chars)
    print('\nThe decoded message is:', message)

main()