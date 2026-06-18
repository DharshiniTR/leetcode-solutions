class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a=sorted(s)
        b=sorted(t)
        s1=""
        s2=""
        for ch in a:
            s1+=ch
        for ch in b:
            s2+=ch
        return s1==s2 
