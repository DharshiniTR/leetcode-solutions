class Solution:
    def removeDuplicates(self, s: str) -> str:
        S=[]
        for ch in s:
            if S and S[-1]==ch:
                S.pop()
            else:
                S.append(ch)
        return "".join(S)
        