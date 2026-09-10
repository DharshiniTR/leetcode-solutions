class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        dp=[0]*(n)
        pre=[0]*(n)
        s=1
        p=1
        for i in range(n):
            pre[i]=p
            p*=nums[i]
        for i in range(n-1,-1,-1):
            pre[i]*=s
            s*=nums[i]
        return pre

        