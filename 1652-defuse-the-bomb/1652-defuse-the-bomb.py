class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n=len(code)
        if k==0:
            return [0]*n
        code*=2
        ans=[0]*n
        if k>0:
            s=sum(code[1:k+1])
            for i in range(n):
                ans[i]=s
                s+=code[i+1+k]-code[i+1]
        else:
            k=-k
            s=sum(code[n-k:n])
            for i in range(n):
                ans[i]=s
                s+=code[n+i]-code[n-k+i]
        return ans