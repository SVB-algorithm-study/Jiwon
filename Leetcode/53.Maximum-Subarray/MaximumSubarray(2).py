class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def maxSum(left, right):
            if left == right:
                return nums[left]

            mid = (left + right) // 2
            left_max = maxSum(left, mid)
            right_max = maxSum(mid + 1, right)

            left_cross_max = float("-inf")
            left_cross_sum = 0
            for i in range(mid, left - 1, -1):
                left_cross_sum += nums[i]
                left_cross_max = max(left_cross_max, left_cross_sum)

            right_cross_max = float("-inf")
            right_cross_sum = 0
            for j in range(mid + 1, right + 1):
                right_cross_sum += nums[j]
                right_cross_max = max(right_cross_max, right_cross_sum)

            cross_max = left_cross_max + right_cross_max
            return max(cross_max, max(left_max, right_max))

        return maxSum(0, len(nums) - 1)
