import random
#  represents a minHeap
class MinHeap:

  
    
    # constructor
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    # this method bubblesUp the heap starting from a index to root
    #  when child is more than the parent swap is made
    def percUp(self,i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2

    # add a new entry to heap
    def insert(self,k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)    
    
    #  bubblesDown the heap starting from a index til leaf
    #  when child is more than the parent, then swap them
    def percDown(self,i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    # finds the index of the child having lesser values.
    def minChild(self,i):
        # check if the current node has only left child
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            # note i*2 is left child, while i*2+1 is right child
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1
        
    # remove the root node from the heap
    def delMin(self):
        # remove the root node.
        retval = self.heapList[1]

        # swap the root node with last element
        self.heapList[1] = self.heapList[self.currentSize]
        # update the size
        self.currentSize = self.currentSize - 1

        # update list
        self.heapList.pop()

        # now, check if heap is still balanced
        self.percDown(1)
        return retval

    # build heap from given list of nums
    def buildHeap(self, alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]

        # starting from the second last level, for all the nodes,
        # check if they are in correct order.
        while (i > 0):
            self.percDown(i)
            i = i - 1

    # return number of entries in heap
    def getSize(self):
        return self.currentSize
        
    def heapsort(self):
        nums = []
        while self.getSize() != 0:
            nums.append(self.delMin())
        self.heapList.extend(nums)
        self.currentSize = len(nums)

def main():
    nums = [random.randrange(1, 50, 1) for i in range(7)] # random list 

# Show the binary heap tree resulting from inserting
# the integers on the list one at a time
    hp = MinHeap()
    for n in nums:
        hp.insert(n)
      
    print('Heap after inserting keys one by one: ',hp.heapList)

# Using the list from the previous question
# show the binary search tree resulting from 
# the list as a parameter to the buildHeap method
    hp = MinHeap()
    hp.buildHeap(nums)
     
    print('Heap after inserting keys from list: ',hp.heapList)

if __name__ =="__main__":
    main()