class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words=s.split()
        if len(pattern)!=len(words):
            return False
        mwp={}
        mpw={}
        for i in range(len(words)):
            c1=words[i]
            c2=pattern[i]
            if c1 in mwp:
                if mwp[c1]!=c2:
                    return False
            else:
                mwp[c1]=c2
            if c2 in mpw:
                if mpw[c2]!=c1:
                   return False
            else:
                mpw[c2]=c1
        return True


        