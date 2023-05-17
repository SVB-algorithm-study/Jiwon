## 🗒️ Problem Description
Julius Caesar protected his confidential information by encrypting it using a cipher. Caesar's cipher shifts each letter by a number of letters. If the shift takes you past the end of the alphabet, just rotate back to the front of the alphabet. In the case of a rotation by 3, w, x, y and z would map to z, a, b and c.

```
Original alphabet:      abcdefghijklmnopqrstuvwxyz
Alphabet rotated +3:    defghijklmnopqrstuvwxyzabc
```

## 📌 Constraints
- `1 <= n <= 100`
- `0 <= k <= 100`
- `s` is a valid ASCII string without any spaces.

## 🤔 How to solve the problem

- Use **dictionary** for the encrypted alphabets
  - `cipherDict()` - function that creates dictionary
  - `lower` - dict for lower encrypted alphabets
  - `upper` - dict for upper encrypted alphabets

## 💡 Complexity of the solution
- **Time Complexity**: O(n), the size of string s
- **Space Complexity**: O(n), the size of string s