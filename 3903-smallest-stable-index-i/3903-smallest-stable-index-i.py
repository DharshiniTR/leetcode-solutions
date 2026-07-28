class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        ans=[]
        for i in range(len(nums)):
            ans.append(max(nums[:i+1])-min(nums[i:]))
        for i in range(len(ans)):
            if ans[i]<=k:
                return i
        else:
            return -1
        