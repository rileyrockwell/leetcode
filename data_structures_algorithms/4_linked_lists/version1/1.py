# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head):
        slow = head
        fast = head

        # while the current pointer of next or the pointer after that is not Null
        while fast and fast.next:
            # slow pointer increases by 1 node
            slow = slow.next
            # fast pointer increases by 2 nodes
            fast = fast.next.next
        
        # return left pointer (slow.val) through right pointer (fast.val)
        return slow


head = [1, 2, 3, 4, 5]
instance = ListNode(head)
# print(instance.val)

head = [1, 2, 3, 4, 5]
solution = Solution().middleNode(ListNode(head))
print(solution.val)