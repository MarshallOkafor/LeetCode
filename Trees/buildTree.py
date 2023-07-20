#!/usr/bin/python3
"""
This is the solution to LeetCode problem 105: 
Construct Binary Tree from Preorder and Inorder Traversal.

Runtime: O(n)
"""
class TreeNode:

    def __init__(self, val=0, left=None, right=None):

        self.val = val
        self.left = left
        self.right = right

class Solution:

    def buildTree(self, preorder, inorder) -> TreeNode:
        """
        :type preorder: list[int]
        :type inorder: list[int]
        """

        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        return root
    
# Driver code
if __name__ == '__main__':

    # Traversal arrays
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    # Solution object
    sol= Solution()
    print(sol.buildTree(preorder, inorder))


