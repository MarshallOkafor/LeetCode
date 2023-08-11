#!/usr/bin/python3
"""
This is the solution to LeetCode problem 323:

Given a graph of n nodes, return the number of 
connected components.
"""

class Solution:

    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: list[list[int]]
        :rtype: int
        """

        par = [i for i in range(n)]
        rank = [1] * n

        # Helper function to find the parent
        # of a node
        def find(n: int) -> int:

            res = n

            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]

            return res
        
        # Helper function to update the rank
        # of the each node
        def union(n1: int, n2: int) -> int:

            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return 0
            
            if rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2] += rank[p1]
            else:
                par[p2] = p1
                rank[p1] += rank[p2]

            return 1
        
        count = n
        for n1, n2 in edges:
            count -= union(n1, n2)

        return count
    
# Driver code
if __name__ == '__main__':

    # Variables, object and function calls
    n = 5
    edges = [[0, 1], [1, 2], [3, 4]]

    sol = Solution()
    print(sol.countComponents(n, edges))