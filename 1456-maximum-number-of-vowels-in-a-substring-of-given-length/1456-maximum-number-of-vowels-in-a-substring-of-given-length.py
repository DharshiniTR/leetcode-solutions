class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        c=0
        v=s[:k]
        for ch in v:
            if ch in "aeiou":
                c+=1
        mx=c
        for i in range(k,len(s)):
            if s[i-k] in "aeiou":
                c-=1
            if s[i] in "aeiou":
                c+=1
            mx=max(mx,c)
        return mx