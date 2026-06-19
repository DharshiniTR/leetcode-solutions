class Solution:
    def hammingWeight(self, n: int) -> int:
        b=""
        while n>0:
            b+=str(n%2)
            n//=2
        return b.count('1')

        