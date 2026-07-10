class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s=0
        for i in range(k):
            s+=nums[i]
        mx=s
        for i in range(k,len(nums)):
            s+=nums[i]-nums[i-k]
            mx=max(mx,s)
        return mx/k
        