class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        c=0
        for row in grid:
            for num in row:
                if num<0:
                    c+=1
        return c
        