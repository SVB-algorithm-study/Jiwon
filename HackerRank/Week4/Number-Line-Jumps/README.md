## 🗒️ Problem Description
You are choreographing a circus show with various animals. For one act, you are given two kangaroos on a number line ready to jump in the positive direction (i.e, toward positive infinity).

The first kangaroo starts at location `x1` and moves at a rate of `v1` meters per jump.
The second kangaroo starts at location `x2` and moves at a rate of `v2` meters per jump.
You have to figure out a way to get both kangaroos at the same location at the same time as part of the show. If it is possible, return YES, otherwise return NO.

## 👉🏻 Example
```
x1=2
v1=1
x2=1
v2=2
```

After one jump, they are both at `x=3`, `(x1+v1=2+1, x2+v2=1+2)`, so the answer is `YES`.

## 🤔 How to solve the problem
- If `x1==x2 and v1!=v2` : Starting point are same, but speed differs
- If `x1!=x2 and v1==v2` : Starting point are diff, but speed is same
- If `(x1<x2 and v1<v2) or (x1>x2 and v1>v2)` : Starting point and speed is both smaller