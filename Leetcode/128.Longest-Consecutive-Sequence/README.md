## 🗒️ Problem Description

Given an unsorted array of integers `nums`, return *the length of the longest consecutive elements sequence.*

You must write an algorithm that runs in `O(n)` time.


## 📌 Constraints:

- `0 <= nums.length <= 105`
- `-109 <= nums[i] <= 109`

## 🤔 How to solve the problem
1. Sort the `nums` array
- `prev` contains previous element number and `curr` is a pointer for current element in array.
- `length` contains the current length of the consecutive elements sequence and `res` is the longest consecutive elements sequence that will be updated by `max()` function comparing with `length`
2. In every looping stage, 
    - If the difference of `prev` and `curr` element is **`1`**, it means ***consecutive element***
  
      => increase `length`
    - If the difference of `prev` and `curr` element is **bigger than `1`**, it is not consecutive element

      => 
      1. update `res` using `max()` with `length`
      2. initialize `length` to `1`
  
  - After checking condition, 1) update `prev` using `curr` 2) increase `curr` to check the next element


## 💡 One line notes for solution
recursive: foreach num, get subseq with num and without num, only include num if prev was less, cache solution of each; dp=subseq length which must end with each num, curr num must be after a prev dp or by itself;