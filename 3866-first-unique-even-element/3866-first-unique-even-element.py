class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        f=Counter(nums)
        for ch in f:
            if f[ch]==1:
                if ch%2==0:
                    return ch
        else:
            return -1
        