  
# Python program of above implementation
def find_min_max(min_value, max_value, value_list):
    list_max = value_list[min_value]
    list_min = value_list[min_value]
     
    # If there is only one element 
    if min_value == max_value:
        list_max = value_list[min_value]
        list_min = value_list[min_value]
        return (list_max, list_min)
         
    # If there is only two element
    elif max_value == min_value + 1:
        if value_list[min_value] > value_list[max_value]:
            list_max = value_list[min_value]
            list_min = value_list[max_value]
        else:
            list_max = value_list[max_value]
            list_min = value_list[min_value]
        return (list_max, list_min)
    else:
         
        # If there are more than 2 elements
        mid_value = int((min_value + max_value) / 2)
        list_max_1, list_min_1 = find_min_max(min_value, mid_value, value_list)
        list_max_2, list_min_2 = find_min_max(mid_value + 1, max_value, value_list)
 
    return (max(list_max_1, list_max_2), min(list_min_1, list_min_2))
 

value_list = [6,9,2,5,8] # values to be searched
max_value = len(value_list) - 1 # 
min_value = 0
list_max, list_min = find_min_max(min_value, max_value, value_list)

print('Min value is: ', list_min)
print('Max value is: ', list_max)