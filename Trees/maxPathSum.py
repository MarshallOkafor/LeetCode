#!/usr/bin/python3
"""
This is the solution to LeetCode problem 124: 
Return the maximum path sum of any non-empty path.

Runtime: O(n)
"""
class TreeNode:

    def __init__(self, val=0, left=None, right=None):

        self.val = val
        self.left = left
        self.right = right

class Solution:

    def maxPathSum(self, root: TreeNode) -> int:

        res = [root.val]

        # Return the max path sum without split
        def dfs(root):
            if not root:
                return 0
            
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            # Compute the split sum of the path
            res[0] = max(res[0], root.val + leftMax + rightMax)

            return root.val + max(leftMax, rightMax)
        
        dfs(root)
        return res[0]
    
# Drvier code
if __name__ == '__main__':

    root = [1, 2, 3]
    # Create the solution object
    sol = Solution()
    print(sol.maxPathSum(root))