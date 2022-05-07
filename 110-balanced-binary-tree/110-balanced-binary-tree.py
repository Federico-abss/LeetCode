# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        global result
        result = True
        
        def bfs(root: Optional[TreeNode]) -> int:
            global result
            if not root or not result:
                return 0
                
            maxLeft = bfs(root.left)
            maxRight = bfs(root.right)
            result = result and abs(maxLeft - maxRight) <= 1
            
            return 1 + max(maxLeft, maxRight)
            
        bfs(root)
        return result
        