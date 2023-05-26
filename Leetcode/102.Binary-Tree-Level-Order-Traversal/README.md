## 🗒️ Problem Description

Given the `root` of a binary tree, return *the level order traversal of its nodes' values.* (i.e., from left to right, level by level).

## 📌 Constraints:
- The number of nodes in the tree is in the range `[0, 2000]`.
- `1000 <= Node.val <= 1000`

## 🤔 How to solve the problem
- `q` is a deque for containing the same level nodes
- Firstly, add node values of `q` to `res` array
- Secondly, update the current level nodes 
- Continue looping until `q` is not empty

- Algorithm used: BFS, implement it with Queue
- Whether then updating the queue, Operate pop for only **length of `q` times!!!!!**