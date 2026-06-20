class Solution:
    def addDigits(self, num: int) -> int:
        
        while num>=10:
            s=0
            while num:
                d=num%10
                s=s+d
                num=num//10
            num=s
        return num
           
        