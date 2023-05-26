class Solution:
    def firstBadVersion(self, n: int) -> int:
        t_pos, f_pos = 0, 0
        l, r = 1, n
        if isBadVersion(0):
            return 1
        while l <= r:
            m = (l + r) // 2
            if not isBadVersion(m):
                f_pos = m
                l = m + 1
            else:
                t_pos = m
                r = m - 1
            if t_pos - f_pos == 1:
                return t_pos
