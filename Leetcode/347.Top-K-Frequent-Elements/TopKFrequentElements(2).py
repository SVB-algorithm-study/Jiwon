from heapq import heappush, heappop


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for n in nums:
            counts[n] -= 1

        heap = []
        for key, value in counts.items():
            heappush(heap, (value, key))

        res = []
        for i in range(k):
            value, key = heappop(heap)
            res.append(key)

        return res
