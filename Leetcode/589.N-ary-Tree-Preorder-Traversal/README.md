## 🗒️ Problem Description

Given the `root` of an n-ary tree, return *the preorder traversal of its nodes' values.*

Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)

## 📌 Constraints:
- The number of nodes in the tree is in the range `[0, 10^4]`.
- `0 <= Node.val <= 104`
- The height of the n-ary tree is less than or equal to `1000`.

## 🤔 How to solve the problem
- Preorder Traverse: ***root => left => right***
- Use **deque** for traversing the **children Nodes.**
