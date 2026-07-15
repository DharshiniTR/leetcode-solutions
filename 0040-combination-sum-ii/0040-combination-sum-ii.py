class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        candidates.sort()
        def dfs(i,path,t):
            
            if t==target:
                ans.append(path[:])
                return
            if t>target:
                return
            
            for j in range(i,len(candidates)):
                if j>i and candidates[j]==candidates[j-1]:
                    continue
                path.append(candidates[j])
                dfs(j+1,path,t+candidates[j])
                path.pop()

        dfs(0,[],0)
        return ans
        