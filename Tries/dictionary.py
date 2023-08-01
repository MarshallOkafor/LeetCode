#!/usr/bin/python3
"""
This is the solution to LeetCode problem 211: 
Design Add and Search Words Data Structure.

"""

class TrieNode():
    """
    The Trie Node class
    """

    def __init__(self):

        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):

        self.root = TrieNode()

    def addWord(self, word: str) -> None:

        cur = self.root

        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.word = True

    def search(self, word: str) -> bool:

        def dfs(j, root):

            cur = root

            for i in range(j, len(word)):
                c = word[i]
                if c == '.':
                    for child in cur.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.word
        
        return dfs(0, self.root)

# Driver code
if __name__ == '__main__':

    # Objects and calls
    obj = WordDictionary()
    obj.addWord('bad')
    obj.addWord('dad')
    obj.addWord('mad')
    print(obj.search('pad'))
    print(obj.search('bad'))
    print(obj.search('.ad'))
    print(obj.search('b..'))