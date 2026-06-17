class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        s=[]
        for num in nums:
            s.append(num*num)
        s.sort()
        return s
        