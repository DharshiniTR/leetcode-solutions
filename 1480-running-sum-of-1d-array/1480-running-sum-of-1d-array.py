class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        l=[]
        s=0
        for num in nums:
            s+=num
            l.append(s)
        return l
        