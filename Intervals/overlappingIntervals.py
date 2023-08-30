#!/usr/bin/python3
"""
This is the solution to LeetCode problem 435:

Given an array of intervals intervals where intervals[i] 
= [starti, endi], return the minimum number of intervals 
you need to remove to make the rest of the intervals non-
overlapping.

Runtime: O(nlogn)
"""

class Solution:

    def overlappingIntervals(self, intervals: list[list[int]]) -> int:

        # Leverage Python sort algorithm to sort the intervals
        intervals.sort(key= lambda i : i[0])
        prevEnd = intervals[0][1] # Start from the end of the first interval
        res = 0 # counter

        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                res += 1
                prevEnd = min(prevEnd, end)

        return res
    
# Driver code
if __name__ == '__main__':

    # Variable, object and function call
    intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
    sol = Solution()
    print(sol.overlappingIntervals(intervals))