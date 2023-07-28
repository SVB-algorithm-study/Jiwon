[Leetcode Link](https://leetcode.com/problems/palindromic-substrings/description/)


## 🗒️ Problem Description

Given a string `s`, return *the number of **palindromic substrings** in it.*
A string is a **palindrome** when it reads the same backward as forward.
A **substring** is a contiguous sequence of characters within the string.


## 📌 Example
#### Example 1:
```
Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
```

#### Example 2:
```
Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
```

## 📌 Constraints
- `1 <= s.length <= 1000`
- `s` consists of lowercase English letters.

## 🤔 How to solve the problem
The idea is the same as the editoral solution -- count the number of palindromes starting from the 'center' of a string.