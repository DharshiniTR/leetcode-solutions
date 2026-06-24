class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        ans=[]
        for num in nums:
            if num and -num in nums:
                ans.append(num)
        if not ans:
            return -1
        else:
            return max(ans)
        