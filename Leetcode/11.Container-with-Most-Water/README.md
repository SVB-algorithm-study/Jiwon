## 🗒️ Problem Description

You are given an integer array height of length `n`. There are `n` vertical lines drawn such that the two endpoints of the ith line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the *maximum amount of water a container can store*.

Notice that you may not slant the container.

## 📌 Constraints:

- `n == height.length`
- `2 <= n <= 105`
- `0 <= height[i] <= 104`

## 💡 One line notes for solution

shrinking window, left/right initially at endpoints, shift the pointer with min height;

## ✨ Key point for the solution
- Start the two pointer `left`=0 and `right`=len(height)-1 to make the width maximum.

- What pointer should be moved?
A pointer that is smaller -> Move it to potentially increase the height.

- **Time Complexity**: `O(n)`