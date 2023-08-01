#!/usr/bin/python3
"""
This is the solution to LeetCode problem 208: 
Implement a Trie (Prefix Tree).

Runtime: O(n)
"""

class TrieNode():
    """
    The TrieNode class
    """

    def __init__(self):

        self.children = {} # Using Python dict
        self.endOfWord = False

class Trie():
    """
    The Trie class that implements that Prefix Tree
    """

    def __init__(self):

        self.root = TrieNode()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """

        cur = self.root

        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.endOfWord = True
    
    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """

        cur = self.root

        for char in word:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        
        return cur.endOfWord
    
    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """

        cur = self.root

        for char in prefix:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        
        return True
    
# Driver code
if  __name__ == '__main__':

    # Objects and calls
    obj = Trie()
    obj.insert('apple')
    print(obj.search('apple'))
    print(obj.search('app'))
    print(obj.startsWith('app'))
    obj.insert('app')
    print(obj.search('app'))