#create a simple program to determine if number is odd or even
#version 1
#num = int(input(" Enter a number: "))
#mod = num % 2
#if mod > 0:
#    print("You picked an odd number.")
#else:
#    print("You picked an even number.")

#version 2
num = int(input("Enter a number to check: "))
check = int(input("Give me a number to divide by: "))

if num % 4 == 0:
    print(num, "is a multiple of 4")
elif num % 2 == 0:
    print(num, "is an even number")
else:
    print(num, "is an odd number")
if num % check  == 0:
    print(num,"divides evenly by", check)
else:
    print(num, "does not divide evenly by", check)
