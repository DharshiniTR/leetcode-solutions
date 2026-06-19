class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        n=str(n)
        freq={}
        for ch in n:
            if ch in freq:
                freq[ch]+=1
            else:
                freq[ch]=1
        m=min(freq.values())
        ans=9
        for ch in freq:
            if freq[ch]==m:
                ans=min(ans,int(ch))
        return ans

                
        