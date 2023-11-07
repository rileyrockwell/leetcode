class Node:
	def __init__(self, data):
		# what type of data structure is data?
		self.data = data
		# is next applicable for both a singly and doubly linked list?
		self.next = None

# Singly linked list
class LinkedList:
	def __init__(self):
		# will None get replace with a value?
		self.head = None

	# adding a node to the linked list?
	def append(self, data):
		# where data is which type of data structure (int, float, str, tuple, list, dict, set)?
		new_node = Node(data)

		# what Boolean does self.head yield?
		if not self.head:
			# if not the head of the linked list, then create the head of the linked list
			self.head = new_node

		# opposite of the Boolean disclosed earlier | the head of the linked list already exists
		else:
			
			# what is current in this context? | current node | why define the current node as the head node?
			current = self.head
			
			# while current.next == True | when does current.next get initialized | w/ "None" for each instance of Node?
			while current.next:
			
				# move to the next node?
				current = current.next
			
			# why create a new node
			current.next = new_node

	def display(self):
		current = self.head
		while current:
			print(current.data, end = " -> ")
			current = current.next

		print("None")


my_list = LinkedList()

my_list.append(1)
my_list.append(2)
my_list.display()

my_list.append(3)
my_list.display()