#!/usr/bin/python3
"""
This is the solution to LeetCode problem 206: 
Reverse Singly-Linked List

Runtime: O(n)
"""
class ListNode(object):
    def __init__(self, val=0, next=None):

        self.val = val
        self.next = next

class Solution(object):

    def iterReverseList(self, head):

        # Iterative solution
        prev, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev
    
    def recReverseList(self, head):

        # Recursive solution
        if not head:
            return None
        
        new_head = head
        if head.next:
            new_head = self.recReverselist(head.next)
            head.next.next = head
        head.next = None

        return new_head
    
    def print_list(self, node):

        # Print the List Nodes
        while node:
            if node.next:
                print(f'{node.val}->', end='')
                node = node.next
            else:
                print(f'{node.val}')
                node = node.next
    
# Driver code 
if __name__ == '__main__':

    # ListNodes: 1->2->3->4->5
    # Create the List Node objects
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    # Create the solution object
    sol = Solution()

    # Call the print_list function
    sol.print_list(head)
    
    # Print the reverse List Nodes
    reversed_node = sol.iterReverseList(head)
    sol.print_list(reversed_node)