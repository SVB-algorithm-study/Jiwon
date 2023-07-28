class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        cans = []
        for n in candidates:
            n_cans = [(n, i) for i in range(0, (target // n) + 1)]
            cans.append(n_cans)
        res = []

        def dfs(i, ele, remain):
            if remain == 0:
                combis = []
                for e in ele:
                    combis.extend([e[0]] * e[1])
                if combis not in res:
                    res.append(combis)

            if i >= len(candidates):
                return

            for can in cans[i]:
                n = can[0] * can[1]

                if n > remain:
                    continue
                ele.append(can)
                dfs(i + 1, ele, remain - n)
                ele.pop()

        for i in range(len(candidates)):
            dfs(i, [], target)

        return res
