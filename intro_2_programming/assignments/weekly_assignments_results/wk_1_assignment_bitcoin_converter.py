# a program that converts bitcoin to dollars (usd)
def convert_bitcoin_to_dollars():
# date and time at which conversion rate for bitcoins to usd happened
    date_time = "As of 8/29/2020 at 4:05pm, bitcoin is currently trading at $"
# user should be prompted to input an amount of bitcoin they have
    user_input_bitcoins_they_have = float(input("Please input the amount of bitcoin you own: "))
#convert bitcoin to dollars 
    convert_bitcoin_to_dollars = user_input_bitcoins_they_have * 11529.10
# output the value of the input amount in dollars based on that conversion rate
    print(date_time, convert_bitcoin_to_dollars, "usd")
convert_bitcoin_to_dollars()