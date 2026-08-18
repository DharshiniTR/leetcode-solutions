# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def f(l,r):
            if l is None and r is None:
                return True
            if l is None or r is None:
                return False
            if l.val!=r.val:
                return False
            return f(l.left,r.left) and f(l.right,r.right)
        if subRoot is None:
            return True
        if root is None:
            return False
        if f(root,subRoot):
            return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
        