'''
# create function with parameters to collect val_list values, min val/max val
def minMax(val_list,min_val,max_val):
# create variable size which it length of val_list
    size = len(val_list)
# base case size is the same as 1 return the values from val_list index position 0
    if size == 1 : 
        return val_list[0],val_list[0]
# find the midpoint to split list in two halves
    midPoint = size // 2

    leftMin,leftMax   = minMax(val_list[:midPoint])
    rightMin,rightMax = minMax(val_list[midPoint:])
    return min(leftMin,rightMin), max(leftMin,rightMin)
val_list = [1,2,3,4,5]
min_val = minMax(val_list,min_val,max_val)
max_val = minMax(val_list,min_val,max_val)

print('Min val: ',min_val)
print('Max val: ',max_val)
'''
def min_max(val_list, min_val=None, max_val=None):

    head, *tail = val_list

    if min_val is None:
        min_val = [head]
    elif head < min_val[-1]:
        min_val.append(head)

    if max_val is None:
        max_val = [head]
    elif head > max_val[-1]:
        max_val.append(head)

    if tail:
        return min_max(tail, min_val, max_val)

    return min_val.pop(), max_val.pop()

if __name__ == "__main__":

    val_list = [2, 0, 2, 7, 5, -1, -2]
    min_val, max_val = min_max(val_list)
    print(val_list, min_val, max_val)

   