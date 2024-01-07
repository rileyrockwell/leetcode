class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

	# let prev_node be the node at position i - 1
	def addNode(self, prev_node, node_to_add):
		node_to_add.next = prev_node.next
		prev_node.next = node_to_add

		return 

	# let prev_node be the node at position i - 1
	def deleteNode(self, prev_node):
		prev_node.next = prev_node.next.next
		
		return 

class LinkedList:
	# traversaL
	def getSum(self, head):
		ans = 0
		while head:
			ans += head.val
			head = head.next

		return ans

	# traversal (recursively)
	def getSum(self, head):
		if not head:
			return 0

		return head.val + self.getSum(head.next)


# head = ListNode(0)
# head.next = ListNode(1)
# head.next.next = ListNode(2)

# head = ListNode(0)
# head.addNode(ListNode(0), ListNode(1)) # b/c you need a reference node (i.e. 0)
# head.addNode(ListNode(1), ListNode(2))

# print(head.next.val)

# print(LinkedList().getSum(head))



# Doubly LinkedList
class ListNode:
	def __init__(self, val):
		self.val = val
		self.next = None
		self.prev = None

class LinkedList:
	# let node be the node at position i
	def addNode(self, node, node_to_add):
		prev_node = self.node_to_add
		self.node_to_add.next = self.node
		self.node_to_add.prev = prev_node

		prev_node.next = self.node_to_add

		self.node.prev = self.node_to_add

	# let node be the node at position i
	def deleteNode(self, node):
		prev_node = self.node.prev
		next = self.node.next

		prev_node.next = next
		next.prev = prev_node

	def addToEnd(node_to_add):
	    node_to_add.next = tail
	    node_to_add.prev = tail.prev
	    tail.prev.next = node_to_add
	    tail.prev = node_to_add

	def removeFromEnd():
	    if head.next == tail:
	        return

	    node_to_remove = tail.prev
	    node_to_remove.prev.next = tail
	    tail.prev = node_to_remove.prev

	def addToStart(node_to_add):
	    node_to_add.prev = head
	    node_to_add.next = head.next
	    head.next.prev = node_to_add
	    head.next = node_to_add

	def removeFromStart():
	    if head.next == tail:
	        return
	    
	    node_to_remove = head.next
	    node_to_remove.next.prev = head
	    head.next = node_to_remove.next

	# head = ListNode(None)
	# tail = ListNode(None)
	# head.next = tail
	# tail.prev = head

	# Dummy Pointers
	def getSum(head):
		ans = 0
		dummy = head
		while dummy:
			ans += dummy.val
			dummy = dummy.next

		# same as before, but we still have a pointer at the head
		return ans


# Write your code here
# Try creating 1 <-> 2 <-> 3
# Test with print()


### GPT ###
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current_node = self.head
        while current_node.next and current_node.next.data != data:
            current_node = current_node.next

        if current_node.next:
            current_node.next = current_node.next.next

    def display(self):
        elements = []
        current_node = self.head
        while current_node:
            elements.append(current_node.data)
            current_node = current_node.next
        print(" -> ".join(map(str, elements)))


# Example usage:
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.prepend(0)
linked_list.display()  # Output: 0 -> 1 -> 2 -> 3

linked_list.delete(3)
linked_list.display()  # Output: 0 -> 1 -> 3
