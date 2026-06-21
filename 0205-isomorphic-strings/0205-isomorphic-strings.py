class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mst={}
        mts={}
        for i in range(len(s)):
            c1=s[i]
            c2=t[i]
            if c1 in mst:
                if mst[c1]!=c2:
                    return False
            else:
                mst[c1]=c2
            if c2 in mts:
                if mts[c2]!=c1:
                    return False
            else:
                mts[c2]=c1
        return True