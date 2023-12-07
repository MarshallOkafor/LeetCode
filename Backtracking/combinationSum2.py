#!/usr/bin/python3
"""
This is the solution to LeetCode problem 40: 

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations 
in candidates where the candidate numbers sum to target. Each number in candidates may only be used once in the 
combination. Note: The solution set must not contain duplicate combinations.

Runtime: O(2^n)
"""

class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        
        candidates.sort()
        res = []

        def backtrack(i, cur, total):

            if total == target:
                res.append(list(cur))
                return 

            if i >= len(candidates) or total > target:
                return 

            cur.append(candidates[i])
            backtrack(i + 1, cur, total + candidates[i])
            cur.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            backtrack(i + 1, cur, total)

        backtrack(0, [], 0)

        return res
    
# Driver code
if __name__ == '__main__':

    sol = Solution()
    candidates = [10,1,2,7,6,1,5] 
    target = 8
    print(sol.combinationSum2(candidates, target))