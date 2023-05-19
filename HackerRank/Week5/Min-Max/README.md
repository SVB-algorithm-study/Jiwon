## 🗒️ Problem Description

You will be given a list of integers, `arr` , and a single integer `k`. You must create an array of length `k` from elements of `arr` such that its unfairness is minimized. Call that array *`arr'`*. Unfairness of an array is calculated as

```
max(arr')-min(arr')
```

Where:
- max denotes the largest integer in *`arr'`*
- min denotes the smallest integer in *`arr'`*


## 📌 Constraints:
- `2 <= n <= 10^5`
- `2 <= k <= n`
- `0 <= arr[i] <= 10^9`


## 🤔 How to solve the problem
- Sort Array: To minimize the unfairness of an array
- Using Sliding Window technique
  - `start`: start pointer of the length `k` array
  - `end`: end pointer of the length `k` array
