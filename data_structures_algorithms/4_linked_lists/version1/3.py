from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        return 1


# build the ListNode object
nodes = [1, 2, 3, 4, 5]
left = 2
right = 4

# build the ListNode object from the given nodes array
head = ListNode(1)
head.next = ListNode(2)

head = ListNode(0)
head.next = ListNode(1)




print(Solution().reverseBetween(head, left, right))