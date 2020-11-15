# create a program to implement a deque using linked list

# create the link Dequeue class
class LinkedDeque: 
	# create node class
	class _Node:
		__slots__ = '_element', '_next'
		#constructor for the node class
		def __init__(self,element,next):
			self._element = element
			self._next = next
	# deque constructor
	def __init__(self):
		self._head = None
		self._tail = None 
		self._size = 0
	# size method
	def __len__(self):
		return self._size
	#  method for empty list
	def is_empty(self):
		return self._size == 0
	# add first element to the start of linked list
	def add_first(self,e):
		newest = self._Node(e,None)
		if self.is_empty():
			self._head = newest
			self._tail = newest
		else:
			newest ._next = self._head
		self._head = newest
		self._size += 1
	# add element to the end of the deque
	def add_last(self,e):
		newest = self._Node(e,None)
		if self.is_empty():
			self._head = newest
			self._tail = newest
		else:
			self._tail._next = newest
		self._tail = newest
		self._size += 1
	# method to delete element from the start of deque
	def remove_first(self):
		if self.is_empty():
			print('Linked list is Empty')
		value = self._head._element
		self._head = self._head._next
		self._size -= 1
		if self.is_empty():
			self._tail = None
		return value
	# method to delete element from the end of the deque
	def remove_last(self):
		if self.is_empty():
			print('Linked List is Empty')
		thead = self._head
		i = 0 
		while i < len(self) - 2:
			thead = thead._next
			i += 1
		self._tail = thead
		thead =thead._next
		value = thead._element
		self._tail._next = None
		self._size -= 1
		return value
	# method to display elements
	def display(self):
		thead = self._head
		while thead:
			print(thead._element,end='-->')
			thead = thead._next
		print()
# main function
def main():
	L = LinkedDeque()
	L.add_last(10)
	L.add_last(20)
	L.add_last(30)
	L.add_last(40)
	L.display()
	print('Deleted: ', L.remove_first())
	L.display()
	L.add_first(70)
	L.display()
	print('Deleted: ', L.remove_last())
	L.display()
	


if __name__ =="__main__":
	main()