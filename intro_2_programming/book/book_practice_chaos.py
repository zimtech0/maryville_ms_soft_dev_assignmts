# A simple program illustrating chaotic behavior.
def main():
    print("This program illustrates a chaotic function")
    x = eval (input("Enter a number between 0 and 1: "))
    y = eval (input("Enter a second number between 0 and 1: "))
    for i in range(int(input("How many numbers should I print? "))):
        x = 3.9 * (x-x*x)
        y = 3.9 * (y-y*y)
        print(x,y)

main()