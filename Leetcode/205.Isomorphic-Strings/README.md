## 🗒️ Problem Description
Given two strings `s` and `t`, determine if they are isomorphic.

Two strings `s` and `t` are isomorphic if the characters in `s` can be replaced to get `t`.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

## 📌 Constraints

- `1 <= s.length <= 5 * 104`
- `t.length == s.length`
- `s` and `t` consist of any valid ascii character.

## 🤔 How to solve the problem
- [Main Idea] If the **each alphabets’ all index(positions) are same**, they are isomorphic
- Use *Dictionary*
  - key: alphabets in the string (with considering the order)
  - value: indexes of the alphabets ~
- If `s_dict.values() == t_dict.values()`, they are isomorphic