class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


    def get_sum1(self, head):
        ans = 0
        while head:
            ans += head.val
            head = head.next

        return ans

    def get_sum(self, head):
        if not head:
            return 0

        return head.val + self.get_sum(head.next)
    
one = ListNode(1)
two = ListNode(2)
three = ListNode(3)
one.next = two
two.next = three
head = one

print("###")
print(two.get_sum(one))


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage
my_linked_list = LinkedList()
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)
# my_linked_list.display()



