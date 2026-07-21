class Solution:
    def countBits(self, n: int) -> List[int]:
        dp=[0]*(n+1)
        for i in range(n+1):
            b=bin(i)[2:]
            c=0
            for ch in b:
                if ch=="1":
                    c+=1
            dp[i]=c
        return dp
        
        