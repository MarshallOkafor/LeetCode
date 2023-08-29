"""
This is the solution to LeetCode problem 57:

Insert newInterval into intervals such that 
intervals is still sorted in ascending order by 
starti and intervals still does not have any 
overlapping intervals (merge overlapping intervals 
if necessary). Return intervals after the insertion.

Runtime: O(n)
"""

class Solution:

    def insert(self, intervals, newInterval):
        """
        :type intervals: list[list[int]]
        :type newInterval: list[int]
        :rtype: list[list[int]]
        """

        res = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals)
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]

        res.append(newInterval)

        return res
    
# Drive code
if __name__ == '__main__':

    # Variable, object and function call
    intervals = [[1, 3], [6, 9]]
    newInterval = [2, 5]
    sol = Solution()
    print(sol.insert(intervals, newInterval))