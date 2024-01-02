# Collaborators: Ray

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 100% RAY
class Solution:
    def deleteDuplicates(self, head):
        # head is a ListNode object?
        dummy = head

        while head != None and head.next != None:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next

        return head



# 100% Ray

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head):
        # iterate over the given ListNode object by isolating each node
        # and checking if the remaining nodes are equivalent...
        while (self.head != None and self.head.next != None):
            if head.val == head.next.val:
                return 1

        return 0


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(2)

