#!/usr/bin/python3
"""
This is the solution to LeetCode problem 21: 
Merge Two Sorted Singly-Linked Lists

Runtime: O(n)
"""

class ListNode(object):

    def __init__(self, val=0, next=None):

        self.val = val
        self.next = next

class Solution(object):

    def mergeTwoList(self, head1, head2) -> object:

        dummy = ListNode()
        tail = dummy

        # Compare the sorted list node items.
        while head1 and head2:
            if head1.val < head2.val:
                tail.next = head1
                head1 = head1.next
            else:
                tail.next = head2
                head2 = head2.next
            tail = tail.next

        # append the remain items of the longer list to 
        # the end of the merged list
        if head1:
            tail.next = head1
        if head2:
            tail.next = head2

        return dummy.next

# Driver code
if __name__ == '__main__':

    # Create the the first sorted List Node objects
    head1 = ListNode(1)
    head1.next = ListNode(2)
    head1.next.next = ListNode(4)

    # Create the second sorted List Node objects
    head2 = ListNode(1)
    head2.next = ListNode(3)
    head2.next.next = ListNode(4)

    sol = Solution()
    mergedNodeHead = sol.mergeTwoList(head1, head2)

    # print the merged sorted linked list
    while mergedNodeHead:
        if mergedNodeHead.next:
            print(f'{mergedNodeHead.val}->', end='')
            mergedNodeHead = mergedNodeHead.next
        else:
            print(f'{mergedNodeHead.val}')
            mergedNodeHead = mergedNodeHead.next