class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq={}
        for ch in nums:
            if ch in freq:
                freq[ch]+=1
            else:
                freq[ch]=1
        for ch in freq:
            if freq[ch]==1:
                return ch
        