class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        s=[]
        for row in accounts:
            s.append(sum(row))
        return max(s)
            