class ListNode:
	def __init__(self, val=0):
		self.val = val
		self.next = None

class LinkedList:
	def getMiddle(self, head):
		slow = head
		fast = head
		while fast and fast.next:
			slow = slow.next
			fast = fast.next.next

		return slow.val


head = ListNode(0)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(4)
head.next.next.next.next.next = ListNode(5)

print(LinkedList().getMiddle(head))