class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        even=[]
        for num in nums:
            if num%2==0:
                even.append(num)
            
        if len(even)==0:
            return -1
        freq={}
        for ch in even:
            if ch in freq:
                freq[ch]+=1
            else:
                freq[ch]=1
        ans=float('inf')
        for ch in freq:
            if freq[ch]==max(freq.values()):
                ans=min(ans,int(ch))
        return ans           

        