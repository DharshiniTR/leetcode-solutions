class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        l=len(isConnected)
        v=set()
        p=0
        for i in range(l):
            if i not in v:
                v.add(i)
                q=deque([i])
                while q:
                    n=q.popleft()
                    for j in range(l):
                        if isConnected[n][j]==1 and j not in v:
                            v.add(j)
                            q.append(j)
                p+=1
        return p