class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sDict = {}
        for c in s:
            if c not in sDict:
                sDict[c] = 1
            else:
                sDict[c] += 1
        tDict = {}
        for c in t:
            if c not in tDict:
                tDict[c] = 1
            else:
                tDict[c] += 1
        for char in sDict:
            if char not in tDict or sDict[char] != tDict[char]:
                return False
        return True