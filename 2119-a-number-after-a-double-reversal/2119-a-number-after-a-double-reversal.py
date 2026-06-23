class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        n=num
        rev=0
        while num>0:
            rev=rev*10+num%10
            num//=10
        rev1=0
        while rev>0:
            rev1=rev1*10+rev%10
            rev//=10
        return rev1==n
        
        