#!/usr/bin/python3
"""
This is the solution to LeetCode problem 19: 
Reorder Singly-Linked List

Runtime: O(n)
"""

class ListNode():

    def __init__(self, val=None, next=None):

        self.val = val
        self.next = next

    def print_nodes(self, node):

        while node:
            if node.next:
                print(f'{node.val}->', end='')
                node = node.next
            else:
                print(f'{node.val}')
                node = node.next

class Solution:

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        # Move right to be n distance away from left
        while n and right:
            right = right.next
            n -= 1

        # Move both left and right until right becomes None
        while right:
            left = left.next
            right = right.next

        # Redirect the left node to the next.next node
        # Recall the that left node is one behind the n distance
        left.next = left.next.next

        return dummy.next
        

# Drive code
if __name__ == '__main__':

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    # Print original linked list
    head.print_nodes(head)

    sol= Solution()
    n = 2
    node = sol.removeNthFromEnd(head, n)

    # Print after removal of nth node from the end
    node.print_nodes(node)