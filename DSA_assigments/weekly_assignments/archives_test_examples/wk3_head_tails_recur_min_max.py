def min_max(list_vals, min_val=None, max_val=None): # function with parameters : list values, min val/max val

    head, *tail = list_vals #implement head/tails to break the list into 2 parts

    if min_val is None: # min test case null/0
        min_val = [head] # assign head part of list to min val
    elif head < min_val[-1]: # if head part of list is greater than min value end of list
        min_val.append(head) # add values from head to min val

    if max_val is None: # max test case null/0
        max_val = [head] # assign head part of list to max val
    elif head > max_val[-1]: # head greater than max value
        max_val.append(head) # add values from head to max val

    if tail: 
        return min_max(tail, min_val, max_val) # return values as paramters to function

    return min_val.pop(), max_val.pop() # remove values from min/max list

if __name__ == "__main__":

    list_vals = [8, 0, 52, 7, 5, -1, -23] # array with values
    min_val, max_val = min_max(list_vals) # assign list values to min/max variable
    print(' Array: ',list_vals,'\n','Min Val: ', min_val,'\n','Max Val: ', max_val) # print results to screen