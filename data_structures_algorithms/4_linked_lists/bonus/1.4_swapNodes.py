# Definition for singly-linked list.

from typing import *

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        return 1

head = ListNode(0)
print(Solution().swapNodes(head, 1))