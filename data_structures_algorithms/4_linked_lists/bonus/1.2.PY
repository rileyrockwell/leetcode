# linked list: fast and slow pointers

from typing import *

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        


head = ListNode(0)
head.next = ListNode(1)
head.next.next = ListNode(2)

print(Solution().removeNthFromEnd(head, 1).val)
print(Solution().removeNthFromEnd(head, 0).next.val)