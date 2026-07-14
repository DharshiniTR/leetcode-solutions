class Solution:
    def removeStars(self, s: str) -> str:
        S=[]
        for ch in s:
            if ch=="*":
                if S:
                    S.pop()
            else:
                S.append(ch)
        return "".join(S)
                
        