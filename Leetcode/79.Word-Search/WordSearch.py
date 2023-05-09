class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):
            # if the left_word is empty
            if i == len(word):
                return True

            # check if valid index
            if (
                r < 0
                or r >= row
                or c < 0
                or c >= col
                or (r, c) in path
                or word[i] != board[r][c]
            ):
                return False

            # record path
            path.add((r, c))

            # search in adjacent cells
            res = (
                dfs(r + 1, c, i + 1)
                or dfs(r - 1, c, i + 1)
                or dfs(r, c + 1, i + 1)
                or dfs(r, c - 1, i + 1)
            )

            # remove path
            path.remove((r, c))

            return res

        for i in range(row):
            for j in range(col):
                if dfs(i, j, 0):
                    return True

        return False
