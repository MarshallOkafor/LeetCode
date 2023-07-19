#!/usr/bin/python3
"""
This is the solution to LeetCode problem 230: 
Kth Smallest Element in a BST.

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
    
    def kthSmallest(self, root: TreeNode, k: int) -> int:

        l = [] # List to hold the elements

        def inorderList(root):
            """
            The inorder traversal of a strict BST produces
            a sorted list.
            """

            if not root:
                return
            inorderList(root.left)
            l.append(root.val)
            inorderList(root.right)
        
        inorderList(root)
        return l[k-1]

# Driver code
if __name__ == '__main__':

    # Arrays
    #root = [2, 1, 3]
    root = [3, 1, 4, None, 2]; k = 1
    # Build the tree
    treeObj = TreeNode()
    #root = treeObj.insertLevelOrder(root, len(root))
    root = treeObj.insertLevelOrder(root, len(root))
    # Print the trees
    #root.preorderTree(root)
    #print()
    root.preorderTree(root)
    print()
    # Check if BST
    sol = Solution()
    #print(sol.isValidBST(root))
    print(sol.kthSmallest(root, k))