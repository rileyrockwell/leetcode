# Definition for singly-linked list.

from typing import *

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:        
        slow = head
        fast = head.next.next

        current_node = head

        node_values = []

        # iterate over every node in the LL
        while current_node:
            node_values.append(current_node.val)

            current_node = current_node.next

        node_set = set(node_values)
        node_list = list(node_set)

        # return node_set

        # build the new linked list (unique values, sorted) using node_set

        # initialize the head of the ListNode

        head = ListNode(node_list[0])

        for value in node_list[1:]:
            head.next = ListNode(value)

        



head = ListNode(0)
head.next = ListNode(2)
head.next.next = ListNode(2)
head.next.next.next = ListNode(1)

print(Solution().deleteDuplicates(head))