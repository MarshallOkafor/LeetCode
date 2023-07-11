#!/usr/bin/python3
"""
This is the solution to LeetCode problem 141: 
Determine if the linked list has a cycle in it.

Runtime: O(n)
"""

class ListNode:

    def __init__(self, val, next=None):

        self.val = val
        self.next = next

class Solution:

    def hasCycle(self, head):

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        
        return False

# Driver code
if __name__ == '__main__':

    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(4)   
    head.next.next.next.next = head.next  

    sol = Solution()
    print(sol.hasCycle(head))