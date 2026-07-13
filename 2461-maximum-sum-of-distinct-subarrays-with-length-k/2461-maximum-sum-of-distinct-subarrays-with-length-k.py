class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        w=nums[:k]
        s=0
        for ch in w:
            s+=ch
        print(s)
        c=Counter(w)
        mx=0
        if len(c)==k:
            mx=s
        for i in range(k,len(nums)):
            s-=nums[i-k]
            
            c[nums[i-k]]-=1
            if c[nums[i-k]]==0:
                del c[nums[i-k]]
            s+=nums[i]
            c[nums[i]]+=1
            if len(c)==k:
                mx=max(s,mx)
             
        return mx


        