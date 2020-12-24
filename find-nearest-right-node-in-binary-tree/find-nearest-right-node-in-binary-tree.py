# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> TreeNode:
        
        H = result = None
        
        def dfs(node, h):
            nonlocal H, result
            
            if not node or result:
                return
            
            if H == h:
                result = node
                return
            
            if node == u:
                H = h
                return
            
            dfs(node.left, h+1)
            dfs(node.right, h+1)
                
        dfs(root, 0)
        return result
            
            
            
            
