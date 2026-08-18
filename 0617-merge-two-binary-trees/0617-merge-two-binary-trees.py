# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
       
        def f(l,r):
            if l is None and r is None:
                return 
            if l is None:
                return r
            if r is None:
                return l
            l.val+=r.val
            l.left=f(l.left,r.left)
            l.right=f(l.right,r.right)
            return l
        return f(root1,root2)
            
        