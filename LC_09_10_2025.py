# 2785. Sort Vowels in a String

class Solution:
    def sortVowels(self, s: str) -> str:
        ind = []
        char = []
        vowels = {"A","E","I","O", "U", 'a', 'e', 'i', 'o', 'u'}
        for i, c in enumerate(s):
            if c in vowels:
                ind.append(i)
                char.append(c)
        
        char.sort()
        s = list(s)
        for i, val in enumerate(ind):
            s[val] = char[i]

        return "".join(s)
