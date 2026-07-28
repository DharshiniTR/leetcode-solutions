class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        c=0
        for i in range(len(nums)):
            n=nums[i]
            while n>0:
                if n%10==digit:
                    c+=1
                n//=10
        return c
        