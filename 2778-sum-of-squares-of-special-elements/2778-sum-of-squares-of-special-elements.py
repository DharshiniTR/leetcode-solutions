class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        ans=[]
        
        for i in range(1,len(nums)+1):
            if (len(nums))%i==0:
                ans.append(nums[i-1]**2)
        
        return sum(ans)
        