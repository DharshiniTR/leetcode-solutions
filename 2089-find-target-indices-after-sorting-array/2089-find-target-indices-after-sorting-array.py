class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[j]<nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]
       
        ans=[]
        for i in range(len(nums)):
            if target==nums[i]:
                ans.append(i)
        return ans
        