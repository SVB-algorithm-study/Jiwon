class Solution:
    def countSubstrings(self, s: str) -> int:
        cnt = 0

        for i in range(len(s)):
            cnt += 1
            for j in range(i + 1, len(s)):
                string = s[i : j + 1]
                if string == string[::-1]:
                    cnt += 1

        return cnt
