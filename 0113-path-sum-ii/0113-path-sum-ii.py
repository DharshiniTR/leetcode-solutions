# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans=[]
        def dfs(root,path,t):
            if not root:
              return 
            path.append(root.val)
            t+=root.val
            if not root.right and not root.left:
                if t==targetSum:
                    ans.append(path[:])
            dfs(root.left,path,t)
            dfs(root.right,path,t)
            path.pop()
        dfs(root,[],0)
        return ans

        