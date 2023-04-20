## 🗒️ Problem Description
Given an `m x n` matrix, return all elements of the matrix in spiral order.

## 📌 Constraints:

- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 10`
- `-100 <= matrix[i][j] <= 100`

## 💡 Complexity of the solution
- **Time Complexity**: `O(m*n)` = the dimension of the matrix
- **Space Complexity**: `O(1)` =  No additional space has been used. The list to store the values doesn't count as additional space(?)

## 💡 One line notes for solution
keep track of visited cells; keep track of boundaries, layer-by-layer;

## ✨ Key point for the solution
- Using four points for assigning boundary to the matrix
  - Four points: `left`, `right`, `top`, `bottom`
- After every looping, shrink the boundary
  - `top` boundary shrinks with subtracting (`top-=1`)
  - `right` boundary shrinks with subtracting (`right-=1`)
  - `bottom` boundary shrinks with adding (`bottom+=1`)
  - `left` boundary shrinks with adding (`left+=1`)
- Loop while the boundary is valid => `left<right and top<bottom`
