class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        p=1
        m=-1
        ans=[]
        for i in range(len(nums)):
            if i%2==0:
                ans.append(p*nums[i])
            else:
                ans.append(m*nums[i])
        return sum(ans)
        