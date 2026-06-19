class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq={}
        for ch in arr:
            if ch in freq:
                freq[ch]+=1
            else:
                freq[ch]=1
        ans=[]
        for ch in freq:
            if freq[ch]==ch:
                ans.append(ch)
        
        if ans:
            return max(ans)
        else:
            return -1        