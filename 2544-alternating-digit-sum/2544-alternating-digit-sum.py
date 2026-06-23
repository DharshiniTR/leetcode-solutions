class Solution:
    def alternateDigitSum(self, n: int) -> int:
        l=[]
        while n>0:
            l.append(n%10)
            n//=10
        l.reverse()
        ans=[]
        p=1
        m=-1
        for i in range(len(l)):
            if i%2==0:
                ans.append(l[i]*p)
            else:
                ans.append(l[i]*m)
        return sum(ans)
