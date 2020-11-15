# create program to implement a stack using linked list

# Class to create nodes of linked list 
class linked_list_node: 
	
	# constructor initializes node automatically 
	def __init__(self,data): 
		self.data = data 
		self.next = None
	
class Stack: 
	
	# head is default NULL 
	def __init__(self): 
		self.head = None
	
	# Checks if stack is same as empty
	def isempty(self): 
		if self.head == None: 
			return True
		else: 
			return False
	
	# Method to add data to the stack (head)
	def push(self,data): 
		
		if self.head == None: 
			self.head=linked_list_node(data) 
			
		else: 
			new_node = linked_list_node(data) 
			new_node.next = self.head 
			self.head = new_node 
	
	# Remove element that is the current head
	def pop(self): 
		
		if self.isempty(): 
			return None
			
		else: 
			# Removes the head node and makes 
			#the preceeding one the new head 
			popped_node = self.head 
			self.head = self.head.next
			popped_node.next = None
			return popped_node.data 
	
	# Returns the head node data 
	def peek(self): 
		
		if self.isempty(): 
			return None
			
		else: 
			return self.head.data 
	
	# Prints stack	 
	def display(self): 
		
		inter_node = self.head 
		if self.isempty(): 
			print("Stack ") 
		
		else: 
			
			while(inter_node != None): 
				
				print(inter_node.data,"->",end = " ") 
				inter_node = inter_node.next
			return
# main function		
def main():	
	
	the_stack = Stack() 
	the_stack.push(6) 
	the_stack.push(11) 
	the_stack.push(25) 
	the_stack.push(9) 
	the_stack.push(33) 

	# Display stack elements 
	the_stack.display() 

	# Print top element of stack 
	print("\nTop element is: ",the_stack.peek()) 

	# Delete top elements of stack 
	the_stack.pop() 
	the_stack.pop() 

	# Display stack elements 
	the_stack.display() 

	# Print top element of stack 
	print("\nTop element is: ", the_stack.peek()) 

if __name__ =="__main__":
	main()

