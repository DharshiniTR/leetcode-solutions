class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s1=""
        s2=""
        vow="AEIOUaeiou"
        for i in range(len(s)//2):
            s1+=s[i]
        for i in range(len(s)//2,len(s)):
            s2+=s[i]
        v1=0
        for ch in s1:
            if ch in vow:
                v1+=1
        v2=0
        for ch in s2:
            if ch in vow:
                v2+=1
        return v1==v2
              