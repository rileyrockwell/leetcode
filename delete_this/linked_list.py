class ListNode:
	def __init__(self, val):
		self.val = val
		self.next = None


one = ListNode(1)
two = ListNode(2)
three = ListNode(3)

one.next = two
two.next = three

print(one.val)
print(one.next.val)
print(one.next.next.val)



one = ListNode(1)
two = ListNode(2)
three = ListNode(3)

one.next = two
two.next = three

print(one.val)
print(one.next.val)
print(two.next.val)


def get_sum(head):
	result = 0
	while head:
		result += head.val
		head = head.next

	return result

print(get_sum(ListNode(1)))