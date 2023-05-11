class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort intervals
        intervals.sort(key=lambda x: x[0])
        answer = [intervals[0]]

        # merge
        for start, end in intervals:
            if answer[-1][1] < start:
                answer.append([start, end])
            else:
                answer[-1][1] = max(answer[-1][1], end)

        return answer
