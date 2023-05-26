## 🗒️ Problem Description
Louise joined a social networking site to stay in touch with her friends. The signup page required her to input a name and a password. However, the password must be strong. The website considers a password to be strong if it satisfies the following criteria:

- Its length is at least `6`.
- It contains at least one digit.
- It contains at least one lowercase English character.
- It contains at least one uppercase English character.
- It contains at least one special character. The special characters are: `!@#$%^&*()-+`

She typed a random string of length `n` in the password field but wasn't sure if it was strong. Given the string she typed, can you find the minimum number of characters she must add to make her password strong?

## 📌 Constraints:
- `1 <= n <= 100`
- All characters in  are in `[a-z]`, `[A-Z]`, `[0-9]`, or `[!@#$%^&*()-+ ]`.

## 🤔 How to solve the problem

- Use Dictionary for checking `4` criteria
  - **`digit`, `lower`, `upper`, `special` **
- Then check **length criteria**: if the length is smaller than ***6***