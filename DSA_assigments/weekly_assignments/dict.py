# python program to illustrate a dictionary

def main():

    # Creating a Dictionary 
    # with Integer Keys 
    dict_with_int_key = {1: 'John', 2: 'Jim', 3: 'Jake'} 
    print("\nDictionary with the use of Integer Keys: ") 
    print(dict_with_int_key) 

    # Creating a Dictionary 
    # with Mixed keys 
    mixed_dict = {'Name': 'Susan', 1: [1, 2, 3, 4]} 
    print("\nDictionary with the use of Mixed Keys: ") 
    print(mixed_dict) 

if __name__ == "__main__":
    main()