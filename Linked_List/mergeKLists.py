#!/usr/bin/python3
"""
This is the solution to LeetCode problem 23: 
Merge K sorted list.

Runtime: O(n)
"""

class ListNode():

    def __init__(self, val, next=None):

        self.val = val
        self.next = None

class Solution():

    def mergeKList(self, lists: list[ListNode]) -> ListNode:

        # handle edge case for empty list of ListNodes
        if not lists or len(lists) == 0:
            return None
        
        # Check that the length of available list
        # to merge is greater that 1
        while len(lists) > 1:
            mergedList = []

            # Iterate with a step size of 2 to
            # grab to lists to merge at each 
            # iteration
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if (i+1) < len(lists) else None
                mergedList.append(self.merge(l1, l2))
            lists = mergedList

        return lists[0]
    
    def merge(self, l1, l2):
        """
        Util funtion to perform the merge of the lists
        """

        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        if l1:
            tail.next = l1
        if l2:
            tail.next = l2

        return dummy.next