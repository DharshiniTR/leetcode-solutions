class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def b(i,subset):
            if i==len(nums):
              ans.append(subset[:])
              return
            subset.append(nums[i])
            b(i+1,subset)
            subset.pop()
            b(i+1,subset)
        b(0,[])
        return ans
    