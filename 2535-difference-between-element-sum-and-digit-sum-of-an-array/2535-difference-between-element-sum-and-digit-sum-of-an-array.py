class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        S=sum(nums)
        a=[]
        for num in nums:
            while num>0:
                a.append(num%10)
                num//=10
        s=sum(a)
        return abs(S-s)

