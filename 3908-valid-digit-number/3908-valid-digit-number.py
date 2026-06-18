class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        num=str(n)
        x=str(x)
        if x in num and num[0]!=x:
            return True
        else:
            return False
        