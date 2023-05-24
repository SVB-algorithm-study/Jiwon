## 🗒️ Problem Description
Two words are `anagrams` of one another if their letters can be rearranged to form the other word.

Given a string, split it into two contiguous substrings of equal length. Determine the minimum number of characters to change to make the two substrings into anagrams of one another.

**Example**
```
s = abccde
```

Break `s` into two parts: 'abc' and 'cde'. Note that all letters have been used, the substrings are contiguous and their lengths are equal. Now you can change 'a' and 'b' in the first substring to 'd' and 'e' to have 'dec' and 'cde' which are anagrams. Two changes were necessary.

## 📌 Constraints:
- `1 <= q <= 100`
- `1 <= |s| <- 10^4`

## 🤔 How to solve the problem
- Use **Dictionary**
- Slice the string in to two pieces, then use **Counter** for counting the alphabets in each two strings.

- Loop over the one of two dictionary and check if *the same key(alphabet) is in the another dictionary*
  - If it is True, subtract *the smaller value* of the two from each values of the two dictionary