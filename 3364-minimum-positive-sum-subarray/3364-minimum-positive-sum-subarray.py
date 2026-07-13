class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        ans=float("inf")
        for k in range(l,r+1):
            s=sum(nums[:k])

            if s>0:
                ans=min(ans,s)
            for i in range(k,len(nums)):
                s-=nums[i-k]
                s+=nums[i]
                if s>0:
                    ans=min(s,ans)
        if ans!=float("inf"):
            return ans
        else:
            return -1
        