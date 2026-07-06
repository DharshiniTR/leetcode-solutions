class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        s=[[0]*n for _ in range(m)]
        t=0
        si=sj=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]!=-1:
                    t+=1
                if grid[i][j]==1:
                    si,sj=i,j

        a=0

        def solve(i,j,c):
            nonlocal a,t
            if i<0 or j<0 or i>=m or j>=n or s[i][j]==1 or grid[i][j]==-1:
                return
            if grid[i][j]==2:
                if c==t:
                  a+=1
                return 
                
            s[i][j]=1
            if solve(i+1,j,c+1):
               return True
            if solve(i-1,j,c+1):
               return True
            if solve(i,j+1,c+1):
               return True
            if solve(i,j-1,c+1):
                return True
            s[i][j]=0
            return False
        
        solve(si,sj,1)
        return a