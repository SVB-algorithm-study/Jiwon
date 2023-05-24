from collections import Counter


def anagram(s):
    # Write your code here
    if len(s) % 2 == 1:
        return -1

    first, second = s[: len(s) // 2], s[len(s) // 2 :]
    first_dict, second_dict = Counter(first), Counter(second)

    for k1, v1 in first_dict.items():
        if k1 in second_dict:
            _min = min(v1, second_dict[k1])
            first_dict[k1] -= _min
            second_dict[k1] -= _min

    return sum(second_dict.values())
