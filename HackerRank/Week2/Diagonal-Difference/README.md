## 💡 One line notes for solution
- Let's say that `n` is the size of the a given square matrix.
- **left-to-right** diagonal array is => `[(m,m) for m in range(n)]`
- **right-to-left** diagonal array is => `[(n-1-m,m) for m in range(n)]`