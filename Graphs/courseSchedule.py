#!/usr/bin/python3
"""
This is the solution to LeetCode problem 207:
Return true if you can finish all courses. 
Otherwise, return false
"""

class Solution(object):

    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        preMap = { i:[] for i in range(numCourses) }
        
        for crs, preq in prerequisites:
            preMap[crs].append(preq)

        visited = set()

        def dfs(crs):

            if crs in visited:
                return False

            if preMap[crs] == []:
                return True

            visited.add(crs)
            for preq in preMap[crs]:
                if not dfs(preq):
                    return False

            visited.remove(crs)
            preMap[crs] = []

            return True

        for crs in range(numCourses):
            if not dfs(crs): 
                return False

        return True
    
# Driver code
if __name__ == '__main__':

    # Variables, objects and function calls
    numCourses = 2
    prerequisites = [[1,0]]

    sol = Solution()
    print(sol.canFinish(numCourses, prerequisites))