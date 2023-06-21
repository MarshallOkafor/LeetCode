#!/urs/bin/python3

"""
Reference: github.com/neetcode-gh/leetcode/tree/main/python 

This code provides a solution to the LeetCode 20 problem - Valid Parentheses

Runtime = O(n)
Space = O(n)
"""

class Solution:

    def isValid(self, s: str) -> bool:

        stack = []
        closeToOpen = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in closeToOpen:
                if stack and stack[-1] == closeToOpen[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return True if not stack else False
    
# Driver code
if __name__ == '__main__':

    sol = Solution()
    s = "((]))"
    print(sol.isValid(s))