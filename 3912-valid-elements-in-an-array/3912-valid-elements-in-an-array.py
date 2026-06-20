class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        ans=[]
        for i in range(len(nums)):
            if i==0 or i==len(nums)-1:
                ans.append(nums[i])
            elif nums[i]>max(nums[:i]):
                ans.append(nums[i])
            elif nums[i]>max(nums[i+1:]):
                ans.append(nums[i])
        return ans
        