class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

class LinkedList:
	# traversal
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

	# let prev_node be the node at position i - 1
	def addNode(self, prev_node, node_to_add):
		node_to_add.next = prev_node.next
		prev_node.next = node_to_add

	# let prev_node be the node at position i - 1
	def deleteNode(self, prev_node):
		prev_node.next = prev_node.next.next
		

head = ListNode(0)
head.next = ListNode(1)
head.next.next = ListNode(2)

print(LinkedList().getSum(head))



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
		next_node = self.node.next

		prev_node.next = next_node
		next_node.prev = prev_node

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