# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    @cache
    def rob(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
            
        left = 0
        right = 0
        if root.left:
            left = self.rob(root.left.left) + self.rob(root.left.right)
        if root.right:
            right = self.rob(root.right.left) + self.rob(root.right.right)
                
        return max(root.val + right + left, self.rob(root.left) + self.rob(root.right))
            