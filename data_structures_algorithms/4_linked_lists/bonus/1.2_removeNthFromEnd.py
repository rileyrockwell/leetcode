# linked lists: fast and slow pointers

from typing import *

class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

class Solution:
	def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
		return "testing"


head = ListNode(0)
print(Solution().removeNthFromEnd(head, 0))