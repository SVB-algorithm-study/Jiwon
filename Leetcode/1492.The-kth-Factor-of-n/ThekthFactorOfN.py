class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = []

        for num in range(1, int(sqrt(n)) + 1):
            if n % num == 0:
                heapq.heappush(factors, num)
                if num**2 != n:
                    heapq.heappush(factors, n // num)

        if len(factors) < k:
            return -1
        for i in range(k):
            factor = heapq.heappop(factors)

        return factor
