#!/usr/bin/python3
"""
This is the solution to LeetCode problem 297: 
Serialize and Deserialize Binary Tree.

Runtime: O(n) + O(n) => for the serialization and deseriaization
"""

class TreeNode:

    def __init__(self, val=0):

        self.val = val
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        res = []

        # Preorder the tree to create the string
        def dfs(node):
            if not node:
                res.append('N')
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return ','.join(res)
    
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        vals = data.split(',')
        self.i = 0

        # Helper function to create the tree from the string
        def dfs():
            if vals[self.i] == 'N':
                self.i += 1
                return None
            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()

            return node
        
        return dfs()
    
# Driver code
if __name__ == '__main__':

    root = [1, 2, 3, None, None, 4, 5] # Has to be TreeNode

    # Codec objec
    ser = Codec()
    deser = Codec()
    ans = deser.deserialize(ser.serialize(root))