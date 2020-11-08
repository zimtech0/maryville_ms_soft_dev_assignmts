#program that simulates rolling two 6-sided dice, and repeatedly rolls them until a target sum is reached
from random import random
from random import seed


# create main function
def main ():
# first random value
    seed(1)
#target value
    target = int(input(" Enter the target number :"))
#count to store number of itereations
    count = 0;
# loop it break
    while True: 
# increment counter
        count =count + 1
# first random number
        value1 = (int(random()*10))% 6 + 1
# second random number
        value2 = (int(random()*10))% 6 + 1
# sum of value 1 and value 2
        sum = value1 + value2
        print("Roll : ",value1, " and ",value2, " sum is ", sum)
# whe sum is reached as target
        if(sum == target):
# stop loop
            break

        print("Got it in  ", count," rolls")



#call main function
main()