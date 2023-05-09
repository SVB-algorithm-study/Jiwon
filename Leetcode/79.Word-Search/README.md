## 🗒️ Problem Description

Given an `m x n` grid of characters `board` and a string `word`, return `true` *if `word` exists in the grid.*

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

## 📌 Constraints
- `m == board.length`
- `n = board[i].length`
- `1 <= m, n <= 6`
- `1 <= word.length <= 15`
- `board` and `word` consists of only lowercase and uppercase English letters.

## 🤔 How to solve the problem
- BackTracking 

## 💡 One line notes for solution
dfs on each cell, for each search remember visited cells, and remove cur visited cell right before you return from dfs;