#!/usr/bin/python3
"""
This is the solution to LeetCode problem 920:

Given an array of meeting time intervals consisting 
of start and end times [[s1,e1],[s2,e2],...] (si < ei), 
determine if a person could attend all meetings.

Runtime: O(nlogn)
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

    def canAttendMeetings(self, intervals):
        """
        :type intervals: list[tuple(int)]
        :rtype: bool
        """

        intervals.sort(key= lambda i : i.start)

        for i in range(1, len(intervals)):
            i1 = intervals[i-1]
            i2 = intervals[i]

            if i1.end > i2.start:
                return False
            
        return True
    
# Driver code
if __name__ == '__main__':

    # Variable, obeject and function call
    array = [[0, 30], [5, 10], [15, 20]]
    obj = Intervals()
    intervals = obj.createIntervals(array)
    print(intervals)
    
    sol = Solution()
    print(sol.canAttendMeetings(intervals))
