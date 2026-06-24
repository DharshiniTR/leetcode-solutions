class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        f=Counter(nums)
        for ch in f:
            if f[ch]==1:
                return ch
        