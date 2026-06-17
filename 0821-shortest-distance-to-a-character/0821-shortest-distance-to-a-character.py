class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        o=[]
        for i in range(len(s)):
            if s[i]==c:
                o.append(i)
        ans=[]
        for i in range(len(s)):
            d=[]
            for ch in o:
                d.append(abs(i-ch))
            ans.append(min(d))
        return ans

            
        