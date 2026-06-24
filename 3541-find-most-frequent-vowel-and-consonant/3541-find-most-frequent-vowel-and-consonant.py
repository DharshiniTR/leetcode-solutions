class Solution:
    def maxFreqSum(self, s: str) -> int:
        f=Counter(s)
        V=[]
        C=[]
        for ch in f:
            if ch in "aeiouAEIOU":
                V.append(f[ch])
            else:
                C.append(f[ch])
        v=max(V) if V else 0
        c=max(C) if C else 0
        return v+c
        