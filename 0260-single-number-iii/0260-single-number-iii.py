class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        ans=[]
        f=Counter(nums)
        for ch in f:
            if f[ch]==1:
                ans.append(ch)
        return ans