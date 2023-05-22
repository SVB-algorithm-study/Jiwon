## 🗒️ Problem Description

Given a string `s` which consists of lowercase or uppercase letters, return *the length of the longest palindrome that can be built with those letters.*

Letters are **case sensitive**, for example, `"Aa"` is not considered a palindrome here.

## 📌 Constraints:

- `1 <= s.length <= 2000`
- `s` consists of lowercase **and/or** uppercase English letters only.

## 🤔 How to solve the problem

- Only **even** numbers of alphabets can be used to create a palindrome
- If there is **one** alphabet, it can be used for the ***middle of the palindrome***