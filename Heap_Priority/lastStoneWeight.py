#!/usr/bin/python3
"""
This is the solution to LeetCode problem 1046: 

You are given an array of integers stones where stones[i] is the weight of the ith stone. We are playing a game with the stones. 
On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with 
x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.

At the end of the game, there is at most one stone left. Return the weight of the last remaining stone. If there are no stones left, 
return 0.

Runtime: O(n)
"""

import heapq

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:

        maxHeap = []

        for stone in stones:
            heapq.heappush(maxHeap, -1 * stone)

        while len(maxHeap) > 1:
            heavy1, heavy2 = -1 * heapq.heappop(maxHeap), -1 * heapq.heappop(maxHeap)
            if heavy1 == heavy2:
                pass
            else:
                heapq.heappush(maxHeap, -1 * (heavy1 - heavy2))

        
        return -1 * maxHeap[0] if maxHeap else 0
    
# Driver code
if __name__ == '__main__':

    sol = Solution()
    stones = [2,7,4,1,8,1]
    print(sol.lastStoneWeight(stones))