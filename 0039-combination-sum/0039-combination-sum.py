class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        def solve(i,s,p):
            if s==target:
                ans.append(p[:])
                return 
            if i>=len(candidates) or s>target:
                return
            p.append(candidates[i])
            solve(i,s+candidates[i],p)
            p.pop()
            solve(i+1,s,p)
        solve(0,0,[])
        return ans