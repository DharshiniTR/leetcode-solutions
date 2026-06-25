class Solution:
    def sumAndMultiply(self, n: int) -> int:
        s=""
        S=0
        while n>0:
            if n%10!=0:
                s=str(n%10)+s
                S+=n%10
            n//=10
        if s!="":
           s=int(s)
           return S*s
        else:
            return 0
       
        