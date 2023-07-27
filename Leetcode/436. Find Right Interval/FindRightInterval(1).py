class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        intervals_index = [(i, e) for i, e in enumerate(intervals)]
        sort_intervals = sorted(intervals_index, key=lambda x: x[1][0])

        answer = {i: 0 for i in range(len(intervals))}

        for i, ele in enumerate(sort_intervals):
            # i is index for binary search
            index, (start, end) = ele
            l, r = i, len(sort_intervals) - 1
            interval = -1

            while l <= r:
                mid = (l + r) // 2
                if sort_intervals[mid][1][0] > end:
                    interval = min(end, sort_intervals[mid][0])
                    r = mid - 1
                elif sort_intervals[mid][1][0] == end:
                    interval = sort_intervals[mid][0]
                    break
                else:
                    l = mid + 1

            answer[index] = interval

        return answer.values()
