class Solution:
    def scoreOfString(self, s: str) -> int:
        ans=[]
        for i in range(len(s)-1):
            ans.append(abs(ord(s[i])-ord(s[i+1])))
        return sum(ans)
        