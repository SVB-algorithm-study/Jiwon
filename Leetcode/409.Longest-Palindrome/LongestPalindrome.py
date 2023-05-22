class Solution:
    def longestPalindrome(self, s: str) -> int:
        alpha_cnt = Counter(s)
        length = 0

        for key, cnt in alpha_cnt.items():
            if cnt >= 2:
                q, r = divmod(cnt, 2)
                length += q * 2
                alpha_cnt[key] = r

        if 1 in alpha_cnt.values():
            length += 1

        return length
