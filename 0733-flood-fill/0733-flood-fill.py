class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        sol=[[0 for _ in range(len(image[0]))] for _ in range(len(image))]
        a=image[sr][sc]
        def solve(x,y):

            if x<0 or y<0 or x>=len(image) or y>=len(image[0]) or image[x][y]!=a or sol[x][y]==1: 
                return False
            
            if image[x][y]==a:
                image[x][y]=color
            sol[x][y]=1
            solve(x+1,y)
            solve(x-1,y)
            solve(x,y+1)
            solve(x,y-1)
            
        solve(sr,sc)
        return image

        