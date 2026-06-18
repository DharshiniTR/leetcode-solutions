class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        fre={}
        for ch in nums:
            if ch in fre:
                fre[ch]+=1
            else:
                fre[ch]=1
        for ch in fre:
            if fre[ch]==1:
               return ch
        