## 🗒️ Problem Description
You are given an `n x n` 2D `matrix` representing an image, rotate the image by **90** degrees (clockwise).

You have to rotate the image **in-place**, which means you have to modify the input 2D matrix directly. **DO NOT** allocate another 2D matrix and do the rotation.

## 📌 Constraints:

- `n == matrix.length == matrix[i].length`
- `1 <= n <= 20`
- `-1000 <= matrix[i][j] <= 1000`

## 💡 Complexity of the solution
- **Time Complexity**: `O(n^2)` = the dimension of the matrix
- **Space Complexity**: `O(1)` =  No additional space has been used. The matrix is rotated in place.

## 💡 One line notes for solution
rotate layer-by-layer, use that it's a square as advantage, rotate positions in reverse order, store a in temp, a = b, b = c, c = d, d = temp;

## ✨ Key point for the solution
- Using four points for assigning boundary to the matrix
  - Four points: `left`=`top`, `right`=`bottom`
- Rotate each element using `tmp` variable
  - To use just one `tmp`, rotate positions in reverse order
- After every looping, shrink the boundary
  - `right` boundary shrinks with subtracting (`right-=1`)
  - `left` boundary shrinks with adding (`left+=1`)
- Loop while the boundary is valid => `left<right`