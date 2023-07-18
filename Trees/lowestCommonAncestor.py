#!/usr/bin/python3
"""
This is the solution to LeetCode problem 235: 
Lowest Common Ancestor.

NB: Jump to the Solution class for answer to the problem.
Runtime: O(log n)
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

    def lowestCommonAncestor(self, root, p, q) -> TreeNode:
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        """
        cur = root

        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur
            
# Driver code
if __name__ == '__main__':

    # Arrays
    root = [3, 4, 5, 1, 2]
    p = 2
    q = 8
    # Tree Nodes
    treeObj = TreeNode()
    root = treeObj.insertLevelOrder(root, len(root))
    # Print the trees
    root.preorderTree(root)
    print()