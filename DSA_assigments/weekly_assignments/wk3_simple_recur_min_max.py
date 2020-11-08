
 # create a simple recursive function to find min/max values   
def min_max(array_vals, min_val=float('inf'), max_val=-float('inf')):
    # Base case, return accumulated result
    if not array_vals:
        return min_val, max_val

    if isinstance(array_vals[0], list):
        # Element is a list, recurse 
        min_val, max_val = min_max(array_vals[0], min_val, max_val)
    else:
        # Element is a number, update current min & max
        min_val = min(min_val, array_vals[0])
        max_val = max(max_val, array_vals[0])

    # Process rest of the elements from list
    return min_max(array_vals[1:], min_val, max_val)
array_vals = [-1,3,2,4,-25,50]
min_val,max_val = min_max(array_vals,min_val=float('inf'), max_val=-float('inf'))
print(' Array Vals: ',array_vals,'\n','Min Val: ',min_val,'\n','Max Val: ',max_val)
