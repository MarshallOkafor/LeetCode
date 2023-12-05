#!/usr/bin/python3
"""
This is the solution to LeetCode problem 150: 

You are given an array of strings tokens that represents an arithmetic expression in a 
Reverse Polish Notation. Evaluate the expression. Return an integer that represents the 
value of the expression.

Runtime => O(1)
"""

class Solution:

    def evalRPN(self, tokens: list[str]) -> int:

        stack = []

        for c in tokens:
            if c == '+':
                stack.append(stack.pop() + stack.pop())
            elif c == '-':
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == '*':
                stack.append(stack.pop() * stack.pop())
            elif c == '/':
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(c))

        return stack[0]  
    
# Driver code
if __name__ == '__main__':

    sol = Solution()
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print(sol.evalRPN(tokens))