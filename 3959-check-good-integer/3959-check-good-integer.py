class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        s=0
        S=0

        while n>0:
            d=n%10
            s+=d
            S+=d**2
            n//=10
        return S-s>=50
        