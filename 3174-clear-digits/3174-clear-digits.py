class Solution:
    def clearDigits(self, s: str) -> str:
        S=[]
        for ch in s:
            if ch.isdigit():
                S.pop()
            else:
                S.append(ch)
        return "".join(S)