class Solution:
    def findLHS(self, nums: List[int]) -> int:
        c={}
        for num in nums:
            c[num]=c.get(num,0)+1
        ans=0
        for num in c:
            if num+1 in c:
                ans=max(ans,c[num]+c[num+1])
        return ans
        