class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)

        for n in nums:
            counts[n] += 1

        sort_counts = sorted(list(counts.items()), key=lambda x: -x[1])
        result = [sort_counts[i][0] for i in range(k)]

        return result
