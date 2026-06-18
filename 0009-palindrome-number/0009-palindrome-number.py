class Solution:
    def isPalindrome(self, x: int) -> bool:
        y=x
        r=0
        while y>0:
            d=y%10
            r=r*10+d
            y=y//10
        if r==x:
            return True
        else:
            return False
        