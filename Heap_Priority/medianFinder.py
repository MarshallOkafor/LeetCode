#!/usr/bin/python3
"""
This is the solution to LeetCode problem 295: 
Find the median from Data.

Efficient method using Python heaps
"""
import heapq

class MedianFinder(object):

    def __init__(self):
        self.small, self.large = [], []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        
        heapq.heappush(self.small, -1 * num)

        # ensure that every num small <= every num large
        if self.small and self.large and (-1 * self.small[0] > self.large[0]):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        # Small is bigger than large
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # Large is bigger than small
        if len(self.large) > len(self.small) + 1:
            val = -1 * heapq.heappop(self.large)
            heapq.heappush(self.small, val)

    def findMedian(self):
        """
        :rtype: float
        """

        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        return (-1 * self.small[0] + self.large[0]) / 2.0
    
# Driver code
if __name__ == '__main__':

    obj = MedianFinder()
    obj.addNum(1)
    obj.addNum(2)
    obj.addNum(4)
    print(obj.findMedian())