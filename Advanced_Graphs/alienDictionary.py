#!/usr/bin/python3
"""
This is the solution to LeetCode problem 269:

Return a strin of the unique letters in the new alien language
sorted in lexicographically increasing order by the new language
rules.

Runtime: O(V)
"""

class Solution:

    def alienOrder(self, words):
        """
        :type words: list[str]
        :rtype: str
        """

        adjList = { c: set() for w in words for c in w }
        
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adjList[w1[j]].add(w2[j])
                    break

        visited = {}
        res = []

        def dfs(c):

            if c in visited:
                return visited[c]
            
            visited[c] = True
            for nei in adjList[c]:
                if dfs(nei):
                    return True
            
            visited[c] = False
            res.append(c)

        for c in adjList:
            if dfs(c):
                return ""
            
        res.reverse()
        return "".join(res)
    
# Driver code
if __name__ == '__main__':

    # Variable, object and function call
    words = ['wrt', 'wrf', 'er', 'ett', 'rftt']
    sol = Solution()
    print(sol.alienOrder(words))