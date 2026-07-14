class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        p={
            ")":"(","]":"[","}":"{"
        }
        S=[]
        c=0
        for ch in s:
            if ch in "(":
                S.append(ch)
            else:
                if S:
                    S.pop()
                else:
                    c+=1

        return c+len(S)     