#!/urs/bin/python3

"""
Reference: github.com/neetcode-gh/leetcode/tree/main/python 

This code provides a solution to the LeetCode 76 problem of 
the minimum window substring

Runtime = O(n)
"""

class Solution:

    def minWin(self, s: str, t: str) -> str:

        if t == "":
            return ""
        
        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(t)
        res, resLen = [-1, -1], float('infinity')
        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            if c in countT and window[c] <= countT[c]:
                have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    # Update the res variable
                    res = [l, r]
                    resLen = (r - l + 1)
                # Decrease the length from the left window
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
            
        l, r = res

        if resLen != float('infinity'):
            return s[l : r + 1]
        else:
            return ""
                
# Driver code
if __name__ == '__main__':

    sol = Solution()
    s = "bbaa"
    t = "aba"
    print(sol.minWin(s, t))