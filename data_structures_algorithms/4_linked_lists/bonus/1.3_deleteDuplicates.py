# Definition for singly-linked list.

from typing import *

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self):
        self.head = None

    # GPT
    def appendValues(self, data):
        new_node = ListNode(data)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # RGR
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        1. extract values from each node
        2. build a list of the values from (1)
        3. call a set on the array from (2)
        4. build a new linked list from the set in (3)
        5. return the new linked list from (4).
        """
        # base case:
        if head.val == None:
            return head.val

        # preprocessing
        current_node = head
        node_values = []

        # 1. extract values from each node; build a list of the values from (1)
        while current_node.next:
            # 2. build a list of values from (1)
            node_values.append(current_node.val)
            current_node = current_node.next

        # 2. build a list of values from (1); append last node value to the array
        node_values.append(current_node.val)

        # 3. call a set on the array from (2); unique and sorted values (b/c deleting duplicates)
        unique_node_values = set(node_values)
        unique_node_values = list(unique_node_values)

        # 4. build a new linked list from the set (turned back into an array) from (3)
        linked_list = Solution()

        for value in unique_node_values:
            linked_list.appendValues(value)

        return linked_list

    def display(self):
        current = self.head
        while current:
            print(current.val, end=" -> ")
            current = current.next
        print("None")


# build the linked list
head = ListNode(0)
head.next = ListNode(0)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(1)

print(Solution().deleteDuplicates(head).display())