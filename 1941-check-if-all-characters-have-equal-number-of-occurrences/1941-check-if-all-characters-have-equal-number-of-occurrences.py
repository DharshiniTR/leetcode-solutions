class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        f=Counter(s)
        ans=[]
        for ch in f:
            ans.append(f[ch])
        for i in range(len(ans)):
            if ans[0]!=ans[i]:
                return False
        else:
            return True