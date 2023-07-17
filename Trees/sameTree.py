#!/usr/bin/python3
"""
This is the solution to LeetCode problem 100: 
Check if two binary trees are thesame.

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

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # Base cases
        if not p and not q:
            return True # Empty nodes are thesame
        if (not p or not q) or (p.val != q.val):
            return False
        
        # Recurse and return
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
             
        

# Driver code
if __name__ == '__main__':

    # Arrays
    p_arr = [1, 2, 3]
    q_arr = [1, 2, 3]
    # Tree Nodes
    treeObj = TreeNode()
    p = treeObj.insertLevelOrder(p_arr, len(p_arr))
    q = treeObj.insertLevelOrder(q_arr, len(q_arr))
    # Print the trees
    p.preorderTree(p)
    print()
    q.preorderTree(q)
    print()
    # Check if the trees are the same
    sol = Solution()
    print(sol.isSameTree(p, q))