class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        ans=[]
        for i in range(len(s)):
            ans.append(s[i:]+s[:i])
        if goal in ans:
            return True
        else:
            return False

        