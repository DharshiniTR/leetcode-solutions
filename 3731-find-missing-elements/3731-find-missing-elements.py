class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in range(min(nums),max(nums)):
            if i not in nums:
                ans.append(i)
        if ans:
            return ans
        else:
            return []
        