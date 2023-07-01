class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res, cur_sum = 0, 0
        prefix_sum = {0: 1}

        for n in nums:
            cur_sum += n

            ## check
            if cur_sum - k in prefix_sum:
                res += prefix_sum[cur_sum - k]

            ## add prefix sum to the hashmap
            if cur_sum in prefix_sum:
                prefix_sum[cur_sum] += 1
            else:
                prefix_sum[cur_sum] = 1

        return res
