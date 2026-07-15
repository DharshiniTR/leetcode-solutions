class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans=[]
        def b(i,path):
            
            if len(path)==k:
                ans.append(path[:])
                return
            if i>n:
                return
            path.append(i)
            b(i+1,path)
            path.pop()
            b(i+1,path)
        b(1,[])
        return ans
        