# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        a=[]
        d={}
        def dfs(node):
            if not node:
                return 0
            d[node.val]=d.get(node.val,0)+1
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        m=max(d.values())
        for ch in d:
            if d[ch]==m:
                a.append(ch)
        return a
        