#!/usr/bin/python3
"""
This is the solution to LeetCode problem 973: 

Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, 
return the k closest points to the origin (0, 0). The distance between two points on the X-Y plane is the Euclidean 
distance (i.e., √(x1 - x2)2 + (y1 - y2)2). You may return the answer in any order. The answer is guaranteed to be 
unique (except for the order that it is in).

Runtime: O(n)
"""

import heapq

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        
        minHeap = []

        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            minHeap.append([dist, x, y])

        heapq.heapify(minHeap)
        res = []
        while k > 0:
            dist, x, y = heapq.heappop(minHeap)
            res.append([x, y])
            k -= 1

        return res

# Driver code
if __name__ == '__main__':

    sol = Solution()
    points = [[1,3],[-2,2]] 
    k = 1
    print(sol.kClosest(points, k))