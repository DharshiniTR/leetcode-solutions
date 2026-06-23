class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        f=Counter(nums)
        ans=[]
        for ch in f:
            if f[ch]==2:
                ans.append(ch)
        s=set(nums)
        for i in range(1,len(nums)+1):
            if i not in s:
                ans.append(i)
        return ans
        