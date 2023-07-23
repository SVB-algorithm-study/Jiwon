class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = {node: [] for node in range(len(isConnected))}

        n = len(isConnected)

        for i in range(n):
            for j in range(i + 1, n):
                if i != j and isConnected[i][j] == 1:
                    graph[i].append(j)
                    graph[j].append(i)

        # DFS - count the province
        visited = set()
        province = 0

        def dfs(node):
            if node in visited:
                return

            visited.add(node)
            if not graph[node]:
                return
            # check the neighbor nodes
            for neigh in graph[node]:
                dfs(neigh)

        for node in graph:
            if node not in visited:
                dfs(node)
                province += 1

        return province
