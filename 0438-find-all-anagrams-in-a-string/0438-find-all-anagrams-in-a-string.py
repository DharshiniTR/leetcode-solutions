class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans=[]
        k=len(p)
        if k>len(s):
            return ans
        w=Counter(s[:k])
        P=Counter(p)
        if w==P:
            ans.append(0)
        for i in range(k,len(s)):
            w[s[i]]+=1
            w[s[i-k]]-=1
            if w==P:
                ans.append(i-k+1)
        return ans


        