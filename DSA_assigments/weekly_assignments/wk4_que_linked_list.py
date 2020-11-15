# implement que using linked list

# A linked list (LL) node  to stre queue entries

class linked_list_node: 
	
	def __init__(self, data): 
		self.data = data 
		self.next = None

# A class to represent a queue 

# The queue, front stores the front node of Linked List
# rear stores the last node of Linked List 
class Queue: 
	
	def __init__(self): 
		self.front = self.rear = None

	def isEmpty(self): 
		return self.front == None
	
	# Method to add an item to the queue 
	def EnQueue(self, item): 
		temp = linked_list_node(item) 
		
		if self.rear == None: 
			self.front = self.rear = temp 
			return
		self.rear.next = temp 
		self.rear = temp 

	# Method to remove an item from queue 
	def DeQueue(self): 
		
		if self.isEmpty(): 
			return
		temp = self.front 
		self.front = temp.next

		if(self.front == None): 
			self.rear = None
# main function
def main():
	q = Queue() 
	q.EnQueue(10) 
	q.EnQueue(20) 
	q.DeQueue() 
	q.DeQueue() 
	q.EnQueue(30) 
	q.EnQueue(40) 
	q.EnQueue(50) 
	q.DeQueue() 
	print("Queue Front:  " + str(q.front.data)) 
	print("Queue Rear:  " + str(q.rear.data)) 

if __name__== '__main__': 
	main()
	
	
