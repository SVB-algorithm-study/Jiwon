class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)

        # make directed graph
        for possi, prev in prerequisites:
            graph[prev].append(possi)

        # traced node for checking cycle
        traced = set()
        # visited node for avoiding repeated cycle check
        visited = set()

        # check if cycle exists
        def dfs(node):
            # cycle exists - current node is traced before!
            if node in traced:
                return False
            if node in visited:
                return True
            # record the traced node
            traced.add(node)
            for neigh in graph[node]:
                if not dfs(neigh):
                    return False
            traced.remove(node)
            visited.add(node)

            return True

        for start in list(graph):
            if not dfs(start):
                return False

        return True
