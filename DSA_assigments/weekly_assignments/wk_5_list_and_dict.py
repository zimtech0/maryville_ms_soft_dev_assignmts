# Python program to demonstrate lists and dictionaries


    # Creating a  empty List 
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

    nested_list = [] 
    print("\nBlank List: ") 
    print(nested_list) 

    # Creating a List of numbers 
    list_of_numbers = [10, 20, 14] 
    print("\nList of numbers: ") 
    print(list_of_numbers) 

    # Creating a List of strings and accessing 
    # using index 
    list_of_strings_with_index = ["Jim", "John", "Jake"] 
    print("\nList Items: ") 
    print(list_of_strings_with_index[0]) 
    print(list_of_strings_with_index[2]) 

    # Creating a Multi-Dimensional List 
    # (By Nesting a nested_list inside a List) 
    nested_list = [['Nested', 'inside'] , ['a nested_list']] 
    print("\nMulti-Dimensional List: ") 
    print(nested_list) 
    
if __name__== "__main__":
    main()