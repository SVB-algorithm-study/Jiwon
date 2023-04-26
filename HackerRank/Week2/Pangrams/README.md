## 🗒️ Problem Description

A pangram is a string that contains every letter of the alphabet. Given a sentence determine whether it is a pangram in the English alphabet. Return either `pangram` or `not pangram` as appropriate.

## 💡 Notes to solve the problem
- `alpha_dict`: Use Hashmap data structure for checking the alphabet
  - key: alphabet(`'a'`~`'z'`)
  - value: 1(`int`)
- Pre-processing for the input string
  - remove spaces and convert it a new string with small letters

- If the `len(string)` is smaller than 26, it cannot be `pangram` => return `not pangram`
- Looping the string and subtract `alpha_dict[alpha]-=1` if the value is `1`
- After finishing the looping, if the `sum(alpha_dict.values())==0`, it means the string contains all alphabets so return `pangram` else `not pangram`
