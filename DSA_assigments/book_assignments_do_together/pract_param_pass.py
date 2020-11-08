
user_input_1 = int(input(" Enter the first number: "))
user_input_2 = int(input(" Enter a second number: "))

def main(user_input_1,user_input_2):
    if user_input_1 % user_input_2 == 0:
        return  True
    else:
        return  False

print("\n",main(user_input_1,user_input_2))