## 🗒️ Problem Description
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have `n` versions `[1, 2, ..., n]` and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API `bool isBadVersion(version)` which returns whether `version` is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.


## 📌 Constraints:
- `1 <= bad <= n <= 231 - 1`


## 🤔 How to solve the problem(1)
- Using **Binary Search algorithm**
- `isBadversion()` => false: good / true: bad
- `f_pos`: pointing good version index(false position)
- `t_pos`: pointing bad version index(true position)

- Update `f_pos` and `t_pos` while binary searching
- Return `t_pos` when the difference between the two pointer is ***1***


## 🤔 How to solve the problem(2)
- Similar problem as ***‘finding Pivot’***
- Ex. `[4, 5, 6, 1, 2, 3]` where pivot is `1`

- Finding the **‘leftmost’** bad version by updating `result`
  - `result`: pointing the bad version
