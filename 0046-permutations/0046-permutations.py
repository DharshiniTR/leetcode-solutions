class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        a=[]
        def p(num,ans):
            if len(num)==0:
                a.append(ans)
                return
            for j in range(len(num)):
                p(num[:j]+num[j+1:],ans+[num[j]])
        p(nums,[])
        return a
        