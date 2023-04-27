## 🗒️ Problem Description

Sean invented a game involving a `2n x 2n` matrix where each cell of the matrix contains an integer. He can reverse any of its rows or columns any number of times. The goal of the game is to maximize the sum of the elements in the `n x n` submatrix located in the upper-left quadrant of the matrix.
Given the initial configurations for `q` matrices, help Sean reverse the rows and columns of each matrix in the best possible way so that the sum of the elements in the matrix's upper-left quadrant is maximal.

## 💡 Notes to solve the problem
- Looping only the matrix's upper-left quadrant, and sum the max number from `[current_position_number, numbers in same position in other 3 quadrant]`
