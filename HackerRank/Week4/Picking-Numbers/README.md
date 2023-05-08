## 🗒️ Problem Description
Given an array of integers, find the longest subarray where the absolute difference between any two elements is less than or equal to `1`.

## 📌Example
```python
a = [1,1,2,2,4,4,5,5,5]
```
There are two subarrays meeting the criterion: `[1,1,2,2]` and `[4,4,5,5,5]`. The maximum length subarray has `5` elements.

## 📌 Constraints:
- `2 <= n <= 100`
- `0 < a[i] < 100`
- `The answer will be >=2` 

## 🤔 How to solve the problem
- The subarray should contain 
  1. **only one number** or
  2. **consecutive two types of number** 
- So the answer could be
  1. **max count number of each element in the array** or 
  2. **max sum of two consecutive two types of number**

## 💡 Algorithm Complexity
- Time Complexity: `O(nlogn)` for sorting the array
- Space Complexity: `O(n)`