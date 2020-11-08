INF = float('inf')


# Divide & Conquer solution to find minimum and maximum number in a list

def newmethod499():
    def find_min_max(list_values, front_of_list, back_of_list, min_value, max_values):

    	# if list contains only one element

    	if front_of_list == back_of_list:		   # common comparison

    		if min_value > list_values[back_of_list]:	  # comparison 1
    			min_value = list_values[back_of_list]

    		if max_values < list_values[front_of_list]:	   # comparison 2
    			max_values = list_values[front_of_list]

    		return min_value, max_values

    	# if list contains only two elements

    	if back_of_list - front_of_list == 1:	   # common comparison

    		if list_values[front_of_list] < list_values[back_of_list]:  # comparison 1
    			if min_value > list_values[front_of_list]:   # comparison 2
    				min_value = list_values[front_of_list]

    			if max_values < list_values[back_of_list]:  # comparison 3
    				max_values = list_values[back_of_list]

    		else:
    			if min_value > list_values[back_of_list]:  # comparison 2
    				min_value = list_values[back_of_list]

    			if max_values < list_values[front_of_list]:   # comparison 3
    				max_values = list_values[front_of_list]

    		return min_value, max_values

    	# find mid element
    	mid = (front_of_list + back_of_list) // 2

    	# recur for front_of_list sublist
    	min_value, max_values = find_min_max(list_values, front_of_list, mid, min_value, max_values)

    	# recur for back_of_list sublist
    	min_value, max_values = find_min_max(list_values, mid + 1, back_of_list, min_value, max_values)

    	return min_value, max_values


    if __name__ == '__main__':

    	list_values = [9,6,8,3,2,5,7,1,4]

    	# initialize the minimum element by infinity and the
    	# maximum element by minus infinity
    	(min_value, max_values) = (INF, -INF)
    	(min_value, max_values) = find_min_max(list_values, 0, len(list_values) - 1, min_value, max_values)

    	print("The minimum element in the list is", min_value)
    	print("The maximum element in the list is", max_values)

newmethod499()
