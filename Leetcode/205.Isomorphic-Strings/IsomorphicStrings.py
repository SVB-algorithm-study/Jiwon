class Solution:
    def createDict(self, string):
        str_dict = {s: [] for s in dict.fromkeys(string)}

        for i, alpha in enumerate(string):
            str_dict[alpha].append(i)

        return str_dict

    def isIsomorphic(self, s: str, t: str) -> bool:
        s_dict = self.createDict(s)
        t_dict = self.createDict(t)

        return list(s_dict.values()) == list(t_dict.values())
