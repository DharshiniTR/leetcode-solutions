from collections import deque
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        g=[[] for _ in range(n)]
        for u,v in edges:
            g[u].append(v)
            g[v].append(u)
        v=set()
        q=deque([source])
        v.add(source)
        while q:
            n=q.popleft()
            if n==destination:
                return True
            for nei in g[n]:
                if nei not in v:
                    v.add(nei)
                    q.append(nei)
        return False
        
