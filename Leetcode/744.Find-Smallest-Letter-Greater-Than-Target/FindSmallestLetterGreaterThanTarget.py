class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l, r = 0, len(letters) - 1
        answer = letters[0]

        while l <= r:
            mid = (l + r) // 2

            if letters[mid] > target:
                answer = letters[mid]
                r -= 1
            else:
                l += 1

        # if not exist
        return answer
