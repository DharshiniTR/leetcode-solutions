class Solution:
    def reverseBits(self, n: int) -> int:
        rev=""
        s=bin(n)[2:].zfill(32)
        for i in range(len(s)-1,-1,-1):
            rev+=s[i]
        return int(rev,2)

        