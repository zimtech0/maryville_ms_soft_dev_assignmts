def reverse_list(num_list):
    # base case
    if not num_list: # this will be true if num_list == []
        return num_list
    return num_list[-1:] + reverse_list(num_list[:-1]) # recursive case

# array values
num_list = [1,2,3,4,5]
reverse_list(num_list)
print('Initial List: ',num_list,'\n')

print('Reversed List: ',reverse_list(num_list)) # [5, 4, 3, 2, 1]