# Python program for implementation of Selection sort

import sys 

def selection_sort(A):
   

# Traverse through all array elements 
    for i in range(len(A)): 
	
	# Find the minimum element in remaining 
	# unsorted array 
	    min_idx = i 
	    for j in range(i+1, len(A)): 
		    if A[min_idx] > A[j]: 
			    min_idx = j 
			
	# Swap the found minimum element with 
	# the first element		 
	    A[i], A[min_idx] = A[min_idx], A[i] 

# main function
def main():

    A = [1,2,3,4,5,6,7,8,9,10] 
    
    selection_sort(A)

    print ("Sorted array") 
    for i in range(len(A)): 
	    print("%d" %A[i]), 

if __name__== "__main__":
    main()