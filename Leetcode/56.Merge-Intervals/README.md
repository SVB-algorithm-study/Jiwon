## 🗒️ Problem Description
Given an array of `intervals` where `intervals[i] = [starti, endi]`, merge all overlapping intervals, and return *an array of the non-overlapping intervals that cover all the intervals in the input.*

## 📌 Constraints:

- `1 <= intervals.length <= 104`
- `intervals[i].length == 2`
- `0 <= starti <= endi <= 104`

## 🤔 How to solve the problem

1. Sort intervals 
  => `start1` is always smaller than `start2`
2. So, **not overlapping** is when `end1 < start2`
3. **When overlapping**, we have to update only `end1`

## 📌 Algorithm Complexity
- **Time Complexity**: `O(nlogn)` for Sorting
- **Space Complexity**: `O(n)`, size of intervals