#!/usr/bin/python3
"""
This is the solution to LeetCode problem 102: 
Lowest Common Ancestor.

NB: Jump to the Solution class for answer to the problem.
Runtime: O(n)
"""
import collections
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

        if root is None:
            return 
        # Print the root node
        print(root.val, end=' ')
        self.preorderTree(root.left)
        self.preorderTree(root.right)

class Solution:

    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        
        # Use a queue data structure
        q = collections.deque()
        res = []
        q.append(root)
        while q:
            q_length = len(q)
            l = []
            for i in range(q_length):
                node = q.popleft()
                if node:
                    l.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if l:
                res.append(l)
        return res
            
# Driver code
if __name__ == '__main__':

    # Arrays
    root = [3, 9, 20, None, None, 15, 7]
    # Tree Nodes
    treeObj = TreeNode()
    root = treeObj.insertLevelOrder(root, len(root))
    treeObj.preorderTree(root)
    print()
    # Solution
    sol = Solution()
    print(sol.levelOrder(root))