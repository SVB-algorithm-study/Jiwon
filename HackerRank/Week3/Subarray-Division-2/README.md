## 🗒️ Problem Description
Two children, Lily and Ron, want to share a chocolate bar. Each of the squares has an integer on it.

Lily decides to share a contiguous segment of the bar selected such that:

The length of the segment matches Ron's birth month, and,
The sum of the integers on the squares is equal to his birth day.
Determine how many ways she can divide the chocolate.

## 🤔 How to solve the problem
1. Looping over the string until `len(s)-m+1`
2. In every looping, slice the string for current index(`i`) to `i+m`
3. If the sum is same as `d`, add `cnt+1`

