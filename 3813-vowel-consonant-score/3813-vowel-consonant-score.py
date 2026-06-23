class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        v=0
        c=0
        for ch in s:
            if ch in "aeiouAEIOU":
                v+=1
            elif ch.isalpha() and ch not in "aeiouAEIOU":
                c+=1
        if c>0:
           return v//c
        if c==0:
            return 0

        