class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq={}
        for ch in nums:
            if ch in freq:
                freq[ch]+=1
            else:
                freq[ch]=1
        ans=0
        m=0
        for ch in freq:
            if freq[ch]>m:
                m=freq[ch]
                ans=ch
        return ans

            
            
        