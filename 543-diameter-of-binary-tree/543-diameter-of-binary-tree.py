# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        global diameter
        diameter = 0
        
        def dfs(root: Optional[TreeNode], level: int) -> int:
            if not root: 
                return level - 1
            
            left = dfs(root.left, level+1)
            right = dfs(root.right, level+1)
            
            global diameter
            diameter = max(diameter, right + left - 2 * level)
            return max(right, left)
        
        dfs(root, 0)
        return diameter