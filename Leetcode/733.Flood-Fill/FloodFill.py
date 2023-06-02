class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        visited = set()
        start = image[sr][sc]
        row, col = len(image), len(image[0])

        def dfs(r, c):
            if (r, c) in visited:
                return
            if r < 0 or c < 0 or r >= row or c >= col or image[r][c] != start:
                return

            image[r][c] = color
            visited.add((r, c))

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        if start == color:
            return image

        dfs(sr, sc)
        return image
