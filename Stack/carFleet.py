#!/usr/bin/python3
"""
This is the solution to LeetCode problem 853: 

There are n cars going to the same destination along a one-lane road. The destination is target miles away. 
You are given two integer array position and speed, both of length n, where position[i] is the position of 
the ith car and speed[i] is the speed of the ith car (in miles per hour). Return the number of car fleets that 
will arrive at the destination.

Runtime => O(n)
"""

class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        
        pair = [[p, s] for p, s in zip(position, speed)]
        stack = []

        for p, s in sorted(pair)[::-1]:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)
    
# Driver code
if __name__ == '__main__':

    sol = Solution()
    target = 12
    position = [10,8,0,5,3]
    speed = [2,4,1,1,3]
    print(sol.carFleet(target, position, speed))
