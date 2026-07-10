class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        V=s[:k]
        v=0
        for ch in V:
            if ch in "aeiou":
                v+=1
        mx=v
        for i in range(k,len(s)):
            if s[i-k] in "aeiou":
                v-=1
            if s[i] in "aeiou":
                v+=1
            if v>mx:
                mx=v
        return mx
        