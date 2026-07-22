from collections import deque
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        r=len(maze)
        c=len(maze[0])
        s1=entrance[0]
        s2=entrance[1]
        v=set()
        q=deque()
        q.append((s1,s2,0))
        v.add((s1,s2))
        while q:
            i,j,cost=q.popleft()
            if (i==0 or j==0 or j==c-1 or i==r-1) and (i,j)!=(s1,s2):
                return cost
                break
            for di,dj in [(1,0),(-1,0),(0,-1),(0,1)]:
                ni=i+di
                nj=j+dj
                if (0<=ni<r and 0<=nj<c) and (ni,nj) not in v and maze[ni][nj]==".":
                    v.add((ni,nj))
                    q.append((ni,nj,cost+1))
        else:
            return -1
     

        
        