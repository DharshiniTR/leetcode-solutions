class Solution:
    def minimizedStringLength(self, s: str) -> int:
        ans=[]
        for ch in s:
            if ch not in ans:
                ans.append(ch)
        return len(ans)
        