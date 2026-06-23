class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        num=int(num)
        while num>0:
            if int(num)%10==0:
                num//=10
            else:
                return str(num)

        