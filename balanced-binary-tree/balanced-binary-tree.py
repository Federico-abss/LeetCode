# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        
        balanced = True
        
        def dfs(node, h):
            nonlocal balanced
            
            if not node:
                return h
            l = dfs(node.left, h+1)
            r = dfs(node.right, h+1)
            if balanced:
                balanced = abs(l - r) <= 1
            return max(l, r)
        
        dfs(root, 0)
        return balanced
