class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letter_dict = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz",
        }
        res = []

        letters = [letter_dict[int(l)] for l in digits]
        print(letters)

        def dfs(i, ele):
            if len(ele) == len(digits):
                res.append("".join(ele[:]))
            if i == len(digits):
                return

            for letter in letters[i]:
                ele.append(letter)
                dfs(i + 1, ele)
                ele.pop()

        for i in range(len(digits)):
            dfs(i, [])

        return res
