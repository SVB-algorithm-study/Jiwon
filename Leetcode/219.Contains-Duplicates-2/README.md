## 🗒️ Problem Description
Given an integer array `nums` and an integer `k`, return `true` if there are two distinct indices `i` and `j` in the array such that `nums[i] == nums[j]` and `abs(i - j) <= k`.

## 📌 Constraints:
- `1 <= nums.length <= 105`
- `-109 <= nums[i] <= 109`
- `0 <= k <= 105`

## 🤔 How to solve the problem
- The easiest way to identify duplicates: ***HastSet***
  - Insert & Lookup can be done in `O(1)` with using ***HashSet***
- Instead of Brute Force(checking every window),
- Use **Sliding Window** technique

## 💡 One line notes for solution
hashset to get unique values in array, to check for duplicates easily

## 💡 Complexity of the solution
- **Time Complexity**: `O(n)` 
- **Space Complexity**: `O(k)`

