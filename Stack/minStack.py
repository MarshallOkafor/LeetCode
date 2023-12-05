#!/usr/bin/python3
"""
This is the solution to LeetCode problem 155: 

Design a stack that supports push, pop, top, and retrieving the 
minimum element in constant time.

Runtime => O(1)
"""

class MinStack:

    def __init__(self):

        self.stack = []
        self.minStack = []

    def push(self, val) -> None:

        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:

        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:

        return self.stack[-1]
    
    def getMin(self) -> int:

        return self.minStack[-1]
    
# Driver code
if __name__ == '__main__':

    sol = MinStack()
    sol.push(-2)
    sol.push(0)
    sol.push(-3)
    print(sol.getMin())
    sol.pop()
    print(sol.top())
    print(sol.getMin())