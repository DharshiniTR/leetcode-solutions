class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=Counter(nums)
  
        ans=[]
        for ch in sorted(freq,key=freq.get,reverse=True):
            ans.append(ch)
        return ans[:k]
        