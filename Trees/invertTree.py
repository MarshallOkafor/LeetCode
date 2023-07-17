#!/usr/bin/python3
"""
This is the solution to LeetCode problem 226: 
invert a binary tree and return the root

NB: Jump to the Solution class for answer to the problem.
Runtime: O(n)
"""

class TreeNode():
    """
    Class definition for the tree construction
    """

    def __init__(self, val=0, left=None, right=None):

        self.val = val
        self.left = left
        self.right = right

    def insertLevelOrder(self, arr, index, num):
        """
        Util function to create the binary tree using
        BFS
        """

        root = None

        # Base case
        if index < num:
            root = TreeNode(arr[index])
            # Insert left child
            root.left = self.insertLevelOrder(arr, (2 * index + 1), num)
            # Insert right child
            root.right = self.insertLevelOrder(arr, (2 * index + 2), num)

        return root
    
    def preorderTree(self, root):
        """
        Util to print the tree using preorder
        traversal
        """
        
        # Base case
        if not root:
            return
        
        # Traverse tree
        print(root.val, end=' ')
        self.preorderTree(root.left)
        self.preorderTree(root.right)
        
class Solution:

    def invertTree(self, root: TreeNode) -> TreeNode:

        
        # Base case
        if not root:
            return
        # Swap the left and right children
        root.left, root.right = root.right, root.left
        # Recurse
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

# Driver code
if __name__ == '__main__':

    arr = [4, 2, 7, 1, 3, 6, 9]
    index = 0
    # Create a tree object
    treeObj = TreeNode()
    # Build the tree
    root = treeObj.insertLevelOrder(arr, index, len(arr))
    # Print the original tree
    treeObj.preorderTree(root)
    print()

    # Print the inverted tree
    sol = Solution()
    sol.invertTree(root)
    treeObj.preorderTree(root)
    print()