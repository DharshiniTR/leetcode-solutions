class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        s=""
        for num in b:
            s+=str(num)
        s=int(s)
        return pow(a,s,1337)      