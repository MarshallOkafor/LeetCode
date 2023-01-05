#!/bin/python3

class Solution:

    def is_palindrome(self, s: str) -> bool:

        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.is_alphanum(s[l]):
                l += 1
            while r > l and not self.is_alphanum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l+1, r-1

        return True

    def is_alphanum(self, char: str) -> bool:

        return (ord('A') <= ord(char) <= ord('Z') or
                ord('a') <= ord(char) <= ord('z') or
                ord('0') <= ord(char) <= ord('9'))

sol = Solution()
s = 'A man, a plan, a canal: Panama'
print(sol.is_palindrome(s))
