#create main function
def main():
# print program message
    print('This program test if the sequence of positive numbers you input are unique')
# create empty list
    numbers = []
# create unique list variable if unique list
    is_unique_list =True
# print exit program instruction
    print('Enter -1 to quit')
# get user input
    num = int(input('Enter first number: '))
# loop to exit program
    while num != -1:
# loop to determ if list is not unique
        if num in numbers: is_unique_list = False
# add usr input to empty list
        numbers.append(num)
# usr input
        num = int(input('Next: '))
# print either unique or not
    if is_unique_list:
        print('The sequence {} is unique!'.format(numbers))
    else:
        print('The sequence {} is not unique!'.format(numbers))

main()