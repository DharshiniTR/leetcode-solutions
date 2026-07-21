class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        t=0
        ans=len(nums)+1
        for r in range(len(nums)):
            t+=nums[r]
            while t>=target:
                ans=min(ans,r-l+1)
                t-=nums[l]
                l+=1
        if ans==len(nums)+1:
            return 0
        return ans
        