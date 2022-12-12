"""
Given an M x N  grid of characters 'board' and a string 'word',
return True if 'word' exists in the grid.

The approach used in this solution is Backtracking.

Runtime: O(4^n) -> very inefficient
"""

class Solution:
    """
    Solution class to instantiate our object.
    """

    def exists(self, board: list[list[str]], word: str) -> bool:
        """
        The main function to return the result of the backtracking subroutine.
        """

        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):
            """
            The backtracking helper function.
            """

            # Base cases
            if i == len(word):
                return True

            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or word[i] != board[r][c] or (r, c) in path):
                return False

            path.add((r, c))
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))
            path.remove((r, c))

            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True

        return False

# Drive code
if __name__ == '__main__':

    sol = Solution()

    board = [['A', 'B', 'C', 'E'],
             ['S', 'F', 'C', 'S'],
             ['A', 'D', 'E', 'E']]

    word = 'ABCCEDZ'
    print(sol.exists(board, word))
