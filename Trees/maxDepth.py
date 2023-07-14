#!/usr/bin/python3
"""
This is the solution to LeetCode problem 104: 
Maximum depth of a binary tree

NB: Jump to the Solution for answer to the problem.
Runtime: O(n)
"""

class TreeNode():

    def __init__(self, val=0, left=None, right=None):

        self.val = val
        self.left = left
        self.right = right

    def insertLevelOrder(self, arr: list[int], num, index=0):
        """
        Util function to create the binary tree
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

class Solution:

    def maxDepth(self, root):

        # Base case
        if not root:
            return None
        # Use stack approach, iterative DFS
        stack = [[root, 1]]
        res = 0
        # Traverse the tree
        while stack:
            node, depth = stack.pop()
            # Add the children of the node to the stack or not
            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        # Return the max value
        return res

# Driver code
if __name__ == '__main__':

    arr = [1, None, 2]
    treeObj = TreeNode()
    # Build the tree 
    root = treeObj.insertLevelOrder(arr, len(arr))
    # Print the tree in preorder 
    root.preorderTree(root)
    print()
    # Create a solution object
    sol = Solution()
    print('The maximum depth of the tree is', sol.maxDepth(root))