#!/urs/bin/python3

"""
Reference: github.com/neetcode-gh/leetcode/tree/main/python 

This code provides a solution to the LeetCode 121 problem of 
the best time to buy and sell stock

Runtime = O(n)
"""

class Solution():

    def max_profit(self, prices: list[int]) -> int:

        best_profit = 0
        l, r = 0, 1

        while r < len(prices):
            if prices[l] < prices[r]:
                cur_profit = prices[r] - prices[l]
                best_profit = max(best_profit, cur_profit)
            else:
                l = r

            r += 1

        return best_profit

# Driver code
if __name__ == '__main__':

    sol = Solution()
    prices = [7, 1, 5, 3, 6, 4]
    print(sol.max_profit(prices))
