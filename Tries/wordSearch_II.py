#!/usr/bin/python3
"""
This is the solution to LeetCode problem 212: 
Given an m x n board of characters and a list of strings
words, return all words on the board.

"""

class TrieNode():

    def __init__(self):

        self.children = {}
        self.isWord = False

    def addWord(self, word: str) -> None:

        cur = self

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True

class Solution():

    def findWords(self, board, words):
        """
        :type board: list[list[str]]
        :type words: list[str]
        :rtype: list[str]
        """

        # Build the prefix tree
        root = TrieNode()
        for w in words:
            root.addWord(w)

        ROWS, COLS = len(board), len(board[0])
        res, visited = set(), set()

        # Helper function
        def dfs(r, c, node, word):

            # Base case
            if (r < 0 or c < 0 or r == ROWS or c == COLS or 
                (r, c) in visited or board[r][c] not in node.children):
                return
            
            visited.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                res.add(word)

            # Recurse on all legitimate adjacent cells
            dfs(r+1, c, node, word)
            dfs(r-1, c, node, word)
            dfs(r, c+1, node, word)
            dfs(r, c-1, node, word)

            # Trigger backtracking
            visited.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return list(res)
    
# Driver code
if __name__ == '__main__':

    # Variable, object creations and function calls
    board = [["o","a","a","n"],
             ["e","t","a","e"],
             ["i","h","k","r"],
             ["i","f","l","v"]]
    words = ["oath","pea","eat","rain"]
    obj = Solution()
    print(obj.findWords(board, words))