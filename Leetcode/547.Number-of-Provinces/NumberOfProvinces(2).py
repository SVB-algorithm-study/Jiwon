class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)

        # DFS - count the province
        visited = set()
        province = 0

        def dfs(node):
            # check the neighbor nodes
            for i, neigh in enumerate(isConnected[node]):
                if neigh == 1 and i not in visited:
                    visited.add(i)
                    dfs(i)

        for node in range(n):
            if node not in visited:
                dfs(node)
                province += 1

        return province
