#!/usr/bin/python3
"""
Given an array of intervals where intervals[i] = 
[starti, endi], merge all overlapping intervals, 
and return an array of the non-overlapping intervals 
that cover all the intervals in the input.

Runtime: O(nlogn)
"""

class Solution:

    def merge(self, intervals: list[list[int]]) -> list[list[int]]:

        # Sort the intervals by the starting values
        intervals.sort(key=lambda i : i[0])
        res = [intervals[0]] # Update result with the first sorted value in intervals

        for start, end in intervals[1:]:
            lastEnd = res[-1][1]

            if start <= lastEnd:
                res[-1][1] = max(lastEnd, end)
            else:
                res.append([start, end])

        return res
    
# Driver code
if __name__ == '__main__':

    # Variable, object and function call
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    sol = Solution()
    print(sol.merge(intervals))