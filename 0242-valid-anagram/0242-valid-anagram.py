class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        f1=Counter(s)
        f2=Counter(t)
        for ch in s:
            if f1[ch]!=f2[ch]:
                return False
        else:
            return True
