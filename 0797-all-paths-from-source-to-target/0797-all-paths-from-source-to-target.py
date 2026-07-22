class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
    
        ans=[]
        q=deque()
        q.append([0])
        while q:
            path=q.popleft()
            node=path[-1]
            if node==len(graph)-1:
                ans.append(path)
            else:
                for nei in graph[node]:
                    q.append(path+[nei])
        return ans

        