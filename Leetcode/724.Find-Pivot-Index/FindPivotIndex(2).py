class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        right = sum(nums)
        # pivot index starts with 0
        for i, num in enumerate(nums):
            right -= num
            if left == right:
                return i
            left += num
        return -1
