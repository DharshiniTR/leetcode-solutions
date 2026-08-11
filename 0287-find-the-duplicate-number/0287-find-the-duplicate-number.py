class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        l=0
        r=1
        while l<len(nums) and r<len(nums):
            if nums[l]==nums[r]:
                
               return nums[l]
            l+=1
            r+=1


        


            