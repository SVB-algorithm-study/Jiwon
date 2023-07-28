class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(candidates)

        def dfs(cur, cur_sum, idx):  # try out each possible cases
            if cur_sum > target:  # this is the case, cur_sum will never equal to target
                return
            if cur_sum == target:  # if equal, add to `ans`
                ans.append(cur)
                return
            for i in range(idx, n):
                dfs(cur + [candidates[i]], cur_sum + candidates[i], i)  # DFS

        dfs([], 0, 0)
        return ans
