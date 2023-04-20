## 🗒️ Problem Description
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

## 📌 Constraints:

- `m == matrix.length`
- `n == matrix[0].length`
- `1 <= m, n <= 200`
- `-231 <= matrix[i][j] <= 231 - 1`


## 💡 Follow up:

- A straightforward solution using `O(mn)` space is probably a bad idea.
- A simple improvement uses `O(m + n)` space, but still not the best solution.
- Could you devise a constant space solution?

### 🤔 My First Solution

- Space Complexity: `O(m*n)`
  - For `zeros` array that contains zero elements' positions.
  - At worst case, all the element in the array can be zero => `O(m*n)`

### ✨ My Second Solution - Improved Space Complexity

- Space Complexity: `O(n)`
  - For `zeros` dictionary with key `'r'` contains rows where element is zero and key `'c'` contains columns where element is zero.
  - At worst case, all rows or columns of the array can be zero => `O(n)` or `O(m)`

- Decreased memory usage: **Beats 23.93% => Beats 63.17%**