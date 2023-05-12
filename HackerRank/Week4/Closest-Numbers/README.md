## 🗒️ Problem Description
Sorting is useful as the first step in many different tasks. The most common task is to make finding things easier, but there are other uses as well. In this case, it will make it easier to determine which pair or pairs of elements have the smallest absolute difference between them.

## 📌 Example
```
arr = [5, 2, 3, 4, 1]
Sorted, arr' = [1, 2, 3, 4, 5].
```
Several pairs have the minimum difference of `1`
=> `[(1,2), (2,3), (3,4), (4,5)]`

Return the array `[1,2,2,3,3,4,4,5].

## 📌 Constraints
- `2 <= n <= 200000`
- `-10^7 <= arr[i] <= 10^7`
- All `a[i]` are unique in `arr`.

## 🤔 How to solve the problem
- Sort array
- Looping the array until `len(arr)-1`, since we will check the difference between `current & next` element
- Use dictionary 
  - key: difference between `arr[i+1]-arr[i]`
  - value: the pair `(arr[i+1], arr[i])`
