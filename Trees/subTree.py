#!/usr/bin/python3
"""
This is the solution to LeetCode problem 572: 
Check if two binary trees are thesame.

NB: Jump to the Solution class for answer to the problem.
Runtime: O(s*q)
"""
# Import isSameTree as a helper function
from sameTree import Solution

class TreeNode():

    def __init__(self, val=0, left=None, right=None):

        self.val = val
        self.left = left
        self.right = right

    def insertLevelOrder(self, arr: list[int], num, index=0):
        """
        Util function to create the binary tree
        num: length of the array
        """

        if not arr:
            return None
        root = None

        # Build the tree
        if index < num:
            root = TreeNode(arr[index])
            # Insert the left child
            root.left = self.insertLevelOrder(arr, num, (2 * index + 1))
            # Insert the right child
            root.right = self.insertLevelOrder(arr, num, (2 * index + 2))
        return root 
    
    def preorderTree(self, root):
        """
        Util function to traverse the tree and print it in 
        preorder fashion
        """

        if not root:
            return None
        # Print the root node
        print(root.val, end=' ')
        self.preorderTree(root.left)
        self.preorderTree(root.right)

class Solution1:

    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        # Base cases
        if not subRoot:
            return True
        if not root:
            return False
        # Check if they are same tree
        # Call the isSameTree() helper function from the Solution class
        sol = Solution() 
        if sol.isSameTree(root, subRoot):
            return True
        # Continue to check the children of root
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))   

# Driver code
if __name__ == '__main__':

    # Arrays
    root_arr = [3, 4, 5, 1, 2]
    subRoot_arr = [4, 1, 2]
    # Tree Nodes
    treeObj = TreeNode()
    root = treeObj.insertLevelOrder(root_arr, len(root_arr))
    subRoot = treeObj.insertLevelOrder(subRoot_arr, len(subRoot_arr))
    # Print the trees
    root.preorderTree(root)
    print()
    subRoot.preorderTree(subRoot)
    print()
    # Check if the trees are the same
    sol_1 = Solution1()
    print(sol_1.isSubtree(root, subRoot))