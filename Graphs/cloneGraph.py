#!/usr/bin/python3
"""
This is the solution to LeetCode problem 133:
Given a reference of a node in a connected undirected graph.
Return a deep copy (clone) of the graph.
"""
from collections import deque

class Node:

    def __init__(self, val=0, neighbors=None):

        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


    def createGraph(self, adjList: list[list[int]]):

        # Nodes using adjacency list are 1-based
        nodes = [Node(i+1) for i in range(len(adjList))]
        
        for i, neighbors in enumerate(adjList):
            for nei_index in neighbors:
                nodes[i].neighbors.append(nodes[nei_index-1])

        return nodes

    def printGraph(self, node):

        visited = set()
        queue = deque([node])

        while queue:
            current_node = queue.popleft()
            if current_node.val not in visited:
                visited.add(current_node.val)
                neighbor_values = [neighbor.val for neighbor in current_node.neighbors]
                print(str(current_node.val) + '->', neighbor_values)
                queue.extend(current_node.neighbors)

class Solution:

    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """

        oldToNew = {}

        def clone(node):

            if node in oldToNew:
                return oldToNew[node]
            
            copy = Node(node.val)
            oldToNew[node] = copy

            for neighbor in node.neighbors:
                copy.neighbors.append(clone(neighbor))

            return copy
        
        return clone(node) if node else None

# Driver code
if __name__ == '__main__':

    # Create object and make function calls
    adjList = [[2,4],[1,3],[2,4],[1,3]]  
    obj = Node()
    nodes = obj.createGraph(adjList)
    print('Original graph: ')
    obj.printGraph(nodes[0])

    # Solution object and calls for the clone 
    sol = Solution()
    copy = sol.cloneGraph(nodes[0])
    print()
    print('Cloned graph: ')
    obj.printGraph(copy)
