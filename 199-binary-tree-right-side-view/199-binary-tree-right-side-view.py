# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        levels = dict()
        
        def dfs(node: Optional[TreeNode], level: int) -> None:
            if not node:
                return
            
            levels[level] = node.val
            dfs(node.left, level+1)
            dfs(node.right, level+1)
            
        dfs(root, 0)
        return levels.values()