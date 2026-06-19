class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        freq={}
        for ch in str(n):
            if ch in freq:
                freq[ch]+=1
            else:
                freq[ch]=1
        s=0
        for ch in freq:
            s+=int(ch)*freq[ch]
        return s


        