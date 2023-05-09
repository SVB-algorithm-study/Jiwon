## 🗒️ Problem Description

A left rotation operation on an array of size `n` shifts each of the array's elements `1` unit to the left. Given an integer, `d`, rotate the array that many steps left and return the result.

## 📌 Example
```
d = 2
arr = [1,2,3,4,5]
```
After `2` rotations, `arr'=[3,4,5,1,2]`

## 📌 Constraints
- `1 <= n <= 10^5`
- `1 <= d <= n`
- `1 <= a[i] <= 10^6`

## 🤔 How to solve the problem
#### 💡 1. Using extra space - ***Space complexity: `O(n)`***
- Use an extra output array
- Go through every single element and shift it by `k` spaces

#### 💡 2. In-Place solution - ***Space complexity: `O(1)`***
- Main Idea: There are **two portions**.
  - The first portion: will be shifted to the ***end of the array***
  - Last ***len(arr)-k*** elements are going to be shifted to the ***beginning of the array***

1. Reverse the array
2. Reverse eacth 2 portion
  - first `len(arr)-k` elements
  - remaining portions

