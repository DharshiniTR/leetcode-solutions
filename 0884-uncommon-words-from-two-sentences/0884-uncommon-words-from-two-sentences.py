class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s=s1+" "+s2
        f={}
        l=s.split()
        ans=[]
        for word in l:
            if word in f:
                f[word]+=1
            else:
                f[word]=1
        for word in f:
            if f[word]==1:
                ans.append(word)
        return ans

        