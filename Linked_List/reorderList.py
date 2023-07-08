#!/usr/bin/python3
"""
This is the solution to LeetCode problem 146: 
Reorder Singly-Linked List

Runtime: O(n)
"""

class ListNode():

    def __init__(self, val, next=None):

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

class Solution():

    def reorderList(self, head: object) -> object:
        # Find the middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half
        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # Merge the two halves
        first, second = head, prev
        newHead = first # new head of the reordered list
        while second:
            tmp_1, tmp_2 = first.next, second.next
            first.next = second
            second.next = tmp_1
            first, second = tmp_1, tmp_2

        return newHead

# Drive code
if __name__ == '__main__':

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    # Print original linked list
    head.print_nodes(head)

    sol = Solution()
    new_reordered_head = sol.reorderList(head)

    # Print after reordering
    new_reordered_head.print_nodes(new_reordered_head)