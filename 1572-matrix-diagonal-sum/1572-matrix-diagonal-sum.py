class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        s=0
        for i in range(len(mat)):
            s+=mat[i][i]
        S=0
        for i in range(len(mat)):
            if i==i and i==len(mat)-i-1:
                continue
            S+=mat[i][len(mat)-i-1]
            
        return S+s
        