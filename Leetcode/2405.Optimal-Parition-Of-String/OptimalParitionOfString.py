class Solution:
    def partitionString(self, s: str) -> int:
        ans = 1
        partition = set()
        for i in s:
            if i in partition:
                partition = set([i])
                ans += 1
            else:
                partition.add(i)
        return ans
