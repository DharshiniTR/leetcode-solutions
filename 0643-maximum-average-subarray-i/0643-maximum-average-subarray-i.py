class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s=sum(nums[:k])
        mx=s
        for i in range(k,len(nums)):
            s=s-nums[i-k]+nums[i]
            mx=max(s,mx)
        return mx/k
        