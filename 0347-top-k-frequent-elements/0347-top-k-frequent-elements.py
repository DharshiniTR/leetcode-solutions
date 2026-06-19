class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for ch in nums:
            if ch in freq:
                freq[ch]+=1
            else:
                freq[ch]=1
        ans=[]
        for ch in sorted(freq,key=freq.get,reverse=True):
            ans.append(ch)
        return ans[:k]
        