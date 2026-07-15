class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans=[]
        def dfs(i,path,t):
            if t==n:
                if len(path)==k:
                    ans.append(path[:])
                    return
            if t>n:
                return
            for j in range(i,10):
                if j>i and j==j-1:
                   continue
                path.append(j)
                dfs(j+1,path,t+j)
                path.pop()
        dfs(1,[],0)
        return ans

            
        