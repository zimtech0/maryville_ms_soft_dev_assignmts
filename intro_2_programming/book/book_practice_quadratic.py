


n\# A program that computes the real roots of a quadratic equation.
# Illustrates use of the math library.
# Note : This program crashesif the equation has no real roots.

# Makes the math library available
import math

def main():
# Introduction of program to user
		print("This program finds the real solutions to a quadratic ")
# Empty print used a space
		print()
		
#Input Section:
	
#  Variable to capture user input of coefficient a
		a= float(input("Enter coefficient a: "))
#  Variable to capture user input of coefficient b
		b= float(input("Enter coefficient b: "))
#  Variable to capture user input of coefficient c
		c= float(input("Enter coefficient c: "))
		
#Process section:
	
# Variable/Expression to use math library to calculate sqrt
		discRoot = math.sqrt(b * b - 4 * a * c)
		root1 = (-b + discRoot) / (2 * a)
		root2 = (-b - discRoot) / (2 * a)

#Output section:

# Print results to screen
		print()
		print("The solutions are: ",root1 ,root2)
		
#call function
main()
	
