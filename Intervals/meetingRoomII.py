#!/usr/bin/python3
"""
This is the solution to LeetCode problem 919:

Given an array of meeting time intervals consisting 
of start and end times [[s1,e1],[s2,e2],...] (si < ei), 
find the minimum number of conference rooms required.

Runtime: O(nlogn)
Memory: O(n)
"""

class Intervals:

    def __init__(self, start=0, end=0):

        self.start = start
        self.end = end

    def createIntervals(self, arr):

        intervals = []

        for i in arr:
            inter = Intervals(i[0], i[1])
            intervals.append((inter))

        return intervals
    
class Solution:

    def minMeetingRooms(self, intervals):
        """
        :type intervals: list[Intervals_obj]
        :rtype: int
        """

        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        res, count = 0, 0
        s, e = 0, 0

        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1

            res = max(res, count)

        return res
    
# Driver code
if __name__ == '__main__':

    # Variable, object and function call
    array = [[0, 30], [5, 10], [15, 20]]
    obj = Intervals()
    intervals = obj.createIntervals(array)
    print(intervals)
    
    sol = Solution()
    print(sol.minMeetingRooms(intervals))