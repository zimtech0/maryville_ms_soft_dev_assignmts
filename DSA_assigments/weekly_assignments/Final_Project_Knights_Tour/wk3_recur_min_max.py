# create a short function that finds the minimum and maximum values in a sequence without using any loops.
# by splitting list into two and searching and comparing values to find min_value, max_value

INF = float('inf') # variable to assign inf value as float

def find_min_max(list_values,front_of_list,back_of_list,min_value,max_value): #function with parameters
    
    if front_of_list == back_of_list: # base : exit from function calling itself

        if min_value > list_values[back_of_list]: #comparison of values
            min_value = list_values[back_of_list] # assign value(s) to variable min_value

        if max_value < list_values[front_of_list]: #comparison of values
            max_value = list_values[front_of_list] # assign value(s) to variable max_value

        return min_value, max_value # return min and max values

    if back_of_list - front_of_list == 1: # check to see if list contains 2 elements
        
        if list_values[front_of_list] < list_values[back_of_list]: #compare the two list
            if min_value > list_values[front_of_list]: #compare min_value value to front_half_of list
                min_value = list_values[front_of_list] # assign front list values to min_value variable

            if max_value < list_values[back_of_list]: #compare max_value val to back_half_of_list
                max_value = list_values[back_of_list] #assign back list values to max_value variable

        else: 
            if min_value > list_values[back_of_list]: #compare min_value value to back of list
                min_value = list_values[back_of_list] #assign back of list to min_value variable

            if max_value < list_values[front_of_list]: #compare max_value value to front of list
                max_value = list_values[front_of_list] #assign front of list values to max_value variable

        return min_value, max_value # return min_value and max_value values

    mid_value = (front_of_list + back_of_list) // 2 # get to the mid point element floor point 

    min_value, max_value = find_min_max(list_values,front_of_list,mid_value,min_value, max_value) # recur through front part of list

    min_value, max_value = find_min_max(list_values,mid_value + 1,back_of_list,min_value, max_value) # recur through back part of list

    return min_value, max_value # return min_value and max_value values

if __name__ == '__main__': # sets the special __name__ variable to have a value “__main__”
    
    list_values = [8,3,2,5,7,1,4] # list values which will be passes as parameter(s)
    (min_value, max_value) = (INF, -INF) # assigns inf value as , pos/neg
    (min_value, max_value) = find_min_max(list_values, 0, len(list_values) - 1, min_value, max_value)
    

    print("The min value is: ", min_value)
    print("The max value is: ", max_value)



        