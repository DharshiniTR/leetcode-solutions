class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        r=list(s[:3])
        ans=0
        if len(Counter(r))==3:
            ans+=1
        for i in range(3,len(s)):
            r.pop(0)
            r.append(s[i])
            if len(Counter(r))==3:
                ans+=1
        return ans
        
        
               