#!/usr/bin/python3
"""
This is the solution to LeetCode problem 875: 
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. 
The guards have gone and will come back in h hours.Koko can decide her bananas-per-hour eating speed of k. 
Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, 
she eats all of them instead and will not eat any more bananas during this hour.Koko likes to eat slowly but still 
wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

Runtime: O(log n)
"""
import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p/k)

            if hours <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1

        return res
    
# Driver code
if __name__ == '__main__':

    sol = Solution()
    piles = [3,6,7,11] 
    h = 8
    print(sol.minEatingSpeed(piles, h))