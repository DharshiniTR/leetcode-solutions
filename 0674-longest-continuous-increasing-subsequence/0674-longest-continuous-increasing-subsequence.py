class Solution:
    def findLengthOfLCIS(self, nums: list[int]) -> int:
        m=len(nums)
        dp=[1]*(m+1)
        for i in range(1,m):
            if nums[i]>nums[i-1]:
                dp[i]=dp[i-1]+1
        return max(dp)
        