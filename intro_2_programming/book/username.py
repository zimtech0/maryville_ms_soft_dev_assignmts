# create a simple string processing program to generate usernames
# create main function outline
def main():
# get user first and last name
    first_name = input("Please enter your first name (all lowercase): ")
    last_name =  input("Please enter your last name (all lowercase): ")
# concatenate first initial with 7 chars of the last name
    username = first_name [0] + last_name[:7]
# output the username
    print("You're username is: ",username)
# call main function
main()