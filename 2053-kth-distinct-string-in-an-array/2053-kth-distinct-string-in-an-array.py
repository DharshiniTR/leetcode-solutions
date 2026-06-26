class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        ans=[]
        for i in range(len(arr)):
            if arr[i] not in arr[i+1:] and arr[i] not in arr[:i]:
                ans.append(arr[i])
        if k>len(ans):
            return ""
        else:
            return ans[k-1]