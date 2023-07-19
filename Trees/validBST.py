#!/usr/bin/python3
"""
This is the solution to LeetCode problem 98: 
Lowest Common Ancestor.

NB: Jump to the Solution class for answer to the problem.
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
        num: length of the array
        """

        if not arr:
            return None
        root = None

        # Build the tree
        if index < num and arr[index] is not None:
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
            return 
        # Print the root node
        print(root.val, end=' ')
        self.preorderTree(root.left)
        self.preorderTree(root.right)

class Solution:
    
    def isValidBST(self, root: TreeNode) -> bool:

        def valid(node, left, right):
            """
            For valid BST, each node has to respect its left and right 
            boundaries. The highest right boundary value of the left 
            subtree is at the root node. While the lowest left boundary
            of the right subtree is at the root node.
            """

            if not node:
                return True
            if not (node.val > left and node.val < right):
                return False
            # Recursively evaluate the subtrees while respecting the boundaries
            return (valid(node.left, left, node.val) and 
                    valid(node.right, node.val, right))
        
        return valid(root, float('-inf'), float('inf'))

# Driver code
if __name__ == '__main__':

    # Arrays
    #root = [2, 1, 3]
    root2 = [5, 1, 4, None, None, 3, 6]
    # Build the tree
    treeObj = TreeNode()
    #root = treeObj.insertLevelOrder(root, len(root))
    root2 = treeObj.insertLevelOrder(root2, len(root2))
    # Print the trees
    #root.preorderTree(root)
    #print()
    root2.preorderTree(root2)
    print()
    # Check if BST
    sol = Solution()
    #print(sol.isValidBST(root))
    print(sol.isValidBST(root2))
