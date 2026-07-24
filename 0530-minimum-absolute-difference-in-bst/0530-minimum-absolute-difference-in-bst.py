# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        v=[]
        def dfs(node):
            if not node:
                return 0
            dfs(node.left)
            v.append(node.val)
            dfs(node.right)
        dfs(root)
        ans=float("inf")
        for i in range(len(v)-1):
            ans=min(ans,v[i+1]-v[i])
        return ans