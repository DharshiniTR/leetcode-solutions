class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        freq={}
        for ch in nums:
            if ch in freq:
                freq[ch]+=1
            else:
                freq[ch]=1
        s=0
        for ch in freq:
            if freq[ch]==1:
                s+=int(ch)
        return s


        