"""
This returns a list of all unique combinations of candidates where the 
chosen number sum to the target. This is also a variant of the subset sum problem

The approach used in this solution is Backtracking.

Runtime: O(2^n)
"""

class Solution:
    """
    Class to instantiate the solution object.
    """

    def combination_sum(self, candidates: list[int], target: int) -> list[list[int]]:
        """
        This the main function to hold the global result array.
        """
        result = []

        def dfs(i: int, cur: list[int], total: int) -> None:
            """
            This is the subroutine function which does the backtracking 
            to compute all the unique combination sum. It makes two recursive calls on
            each call to itself, thus has an overall exponential runtime.
            """

            # Base cases
            if total == target:
                result.append(list(cur))
                return

            if i >= len(candidates) or total > target:
                return

            # Recursive calls and backtracking
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            cur.pop()
            dfs(i + 1, cur, total)

        # Call to the dfs() subroutine
        dfs(0, [], 0)

        return result

# Driver code
if __name__ == '__main__':

    # Test solution object
    sol = Solution()

    arr = [8, 6, 7, 5, 3, 10, 9]
    target = 15

    print(sol.combination_sum(arr, target))