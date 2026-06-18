class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        p=[]
        n=[]
        for num in nums:
            if num>=1:
                p.append(num)
            elif num<=-1:
                n.append(num)
        if len(p)>len(n):
            return len(p)
        else:
            return len(n)
        