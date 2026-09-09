class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        n=max(nums)
        dp=[0] * (n+1)
        p=[0] * (n+1)
        for x in nums:
            p[x]+=x
        dp[1]=p[1]
        for i in range(2,n+1):
            dp[i]=max(dp[i-1],p[i]+dp[i-2])
        return dp[n]


        