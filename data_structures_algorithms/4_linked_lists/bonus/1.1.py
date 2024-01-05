# Definition for singly-linked list.

# linked lists: fast and slow pointers

from typing import *

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head != None:
            current_node = head
            # given: the LL always contains at least 1 node
            counter = 1
            # while there exists an additional node in the LL
            while current_node.next:
                counter += 1
                current_node = current_node.next

        # def (middle node): len(LL) // 2 + 1
        middle = counter // 2 + 1

        # (1). rebuild the LL w/out the middle node


        # (2). remove the middle node from teh pre-existing LL

    def deleteMiddle(self, head):
        if head == None or head.next == None:
            return None

        # s.t. head is a ListNode object; fast pointer skips 2 nodes
        slow = head
        fast = head.next.next

        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next

        slow.next = slow.next.next

        return head



"""
    public ListNode deleteMiddle(ListNode head) {
        if (head == null || head.next == null) return null;
        ListNode slow = head, fast = head.next.next;
        while (fast != null && fast.next != null) {
            fast = fast.next.next;
            slow = slow.next;
        }
        slow.next = slow.next.next;
        return head;
    }
"""




# head = None
head = ListNode(0)
head.next = ListNode(1)
head.next.next = ListNode(2)

print(Solution().deleteMiddle(head))