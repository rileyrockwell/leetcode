# linked list: fast adnd slow pointers

from typing import *

class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

class Solution:
	def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
		"""
		using fast and slow pointers...
		"""

		slow = self.head
		fast = self.head.next.next

		

		


head = ListNode(0)
print(Solution().deleteMiddle(head))