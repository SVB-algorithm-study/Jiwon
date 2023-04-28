## 🗒️ Problem Description
There is an `m x n` rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an `m x n` integer matrix heights where `heights[r][c]` represents the height above sea level of the cell at coordinate `(r, c)`.

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

*Return a ***2D list*** of grid coordinates result where `result[i] = [ri, ci]` denotes that rain water can flow from cell `(ri, ci)` to both the Pacific and Atlantic oceans.*

## 📌 Constraints:
- `m == heights.length`
- `n == heights[r].length`
- `1 <= m, n <= 200`
- `0 <= heights[r][c] <= 105`

## 🤔 How to solve the problem
- Think and approahc in opposite way!
- Start with the 4 borders of the island that touches Pacific and Atlantic Ocean
- Thinking the solution in opposit way: **Check cells where border cells of the island can reach**
  - 1. Looping the `row=0` for `pac_visited`, `row=m-1` for `atl_visited` => `for i in range(n)`
  - 2. Looping the `column=0` for `pac_visited`, `column=n-1` for `atl_visited` =>  `for j in range(m)`
  - return the cells that are both in `pas_visited` and `atl_visited` using `&` operation


## 💡 One line notes for solution
dfs each cell, keep track of visited, and track which reach pac, atl; dfs on cells adjacent to pac, atl, find overlap of cells that are visited by both pac and atl cells;