class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        if nums[len(nums)//2] not in nums[:len(nums)//2] and nums[len(nums)//2] not in nums[(len(nums)//2)+1:]:
            return True
        else:
            return False
        