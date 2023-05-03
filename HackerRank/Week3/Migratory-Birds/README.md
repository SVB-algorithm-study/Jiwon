## 🗒️ Problem Description
Given an array of bird sightings where every element represents a bird type id, determine the id of the most frequently sighted type. If more than 1 type has been spotted that maximum amount, return the smallest of their ids.

## 🤔 How to solve the problem

- `birds_freq`: Use `Counter()` to get dictionary of array elements counting
- `most_sighted`: Get the sorted list of `birds_freq` with ordering in **2 criteria**
 > 1. frequency of the birds sighted 
 > 2. Sort by the `id` of the birds
- Return the first index of the first element of `most_sighted` list

- Time Complexity: `O(nlogn)` for sorting the list
- Space Complexity: `O(n)`, the size of the array