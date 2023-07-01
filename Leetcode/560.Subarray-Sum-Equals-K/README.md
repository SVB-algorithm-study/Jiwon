[Leetcode Link](https://leetcode.com/problems/subarray-sum-equals-k/description/)

## 🗒️ Problem Description

Given an array of integers `nums` and an integer `k`, return *the total number of subarrays whose sum equals to `k`.*

A subarray is a contiguous **non-empty** sequence of elements within an array.

## 📌 Example
#### Example 1:
```
Input: nums = [1,1,1], k = 2
Output: 2
```
#### Example 2:
```
Input: nums = [1,2,3], k = 3
Output: 2
```

## 📌 Constraints:
- `1 <= nums.length <= 2 * 104`
- `-1000 <= nums[i] <= 1000`
- `-107 <= k <= 107`

## 🤔 How to solve the problem
### 1. Brute Force approach
- Time Complexity: `O(n^2)`

Because there is `n^2` different subarrays in the array, so we have to check every subarray

### 2. Two pointer or Sliding Window

Decrease or increase the size of the total sum of the window

***❗️Problem - check the constraints!***

Values can be negative, so adding a value to a subarray doesn't guarantee increasing the size 

### 3. Improve Brute Force approach to `O(n)`
💡 Main point: Use **Hashmap** to record the ***counts of prefixsum***

=> *Can we somehow be a little bit greedier?*
(1) Can we chop off some prefix of this array such that makes sum match `k`?

(2) Does there exist such prefix in this array?

```
ex)
k=3

sum = 4
sum-k = 4-3 = 1

=> Does `prefix_sum=1` exist in this subarray?
```   

## 💡 Complexity of the solution
- **Time Complexity**: `O(n)` = the length of the array
- **Space Complexity**: `O(n)` = the size of the hashmap

## 💡 What I learned
### `get()` function

- Syntax : `Dict.get(key, default=None)`

- Parameters: 
  - key: The key name of the item you want to return the value from
  - Value: (Optional) Value to be returned if the key is not found. The default value is None.

```python
prefix_sum.get(diff, 0)
```
