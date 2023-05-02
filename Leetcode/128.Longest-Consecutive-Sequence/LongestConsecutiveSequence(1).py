class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        if not nums:
            return 0
        prev = 0
        curr = 1
        length = 1
        res = 1
        while curr < len(nums):
            if nums[curr] - nums[prev] == 1:
                length += 1
            elif nums[curr] - nums[prev] > 1:
                res = max(res, length)
                length = 1
            prev = curr
            curr += 1

        if length != 1:
            res = max(res, length)
        return res
