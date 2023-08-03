class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # check the length of the word in wordDict
        # [3,3,4,3,3]
        # key: length, value: list of words
        # {3: ['dog', 'and', 'cat'],
        #  4: ['cats', 'sand']}
        wordLenDict = defaultdict(list)
        for word in wordDict:
            wordLenDict[len(word)].append(word)

        checked = set()
        breakable = set()

        def checkWord(index, length):
            if (index, length) in checked or index > len(s):
                return

            if index + length >= len(s) and s[index : index + length] in wordDict:
                breakable.add((index, length))
                print("here: ", breakable)
                return

            checked.add((index, length))
            if s[index : index + length] not in wordDict:
                return
            for _len in wordLenDict:
                checkWord(index + length, _len)

        for _len in wordLenDict:
            checkWord(0, _len)

        return breakable
