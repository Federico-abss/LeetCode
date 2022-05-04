# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        global count, result
        count = 0
        
        def dfs(root: Optional[TreeNode]) -> None:
            global count, result
            if count > k or not root:
                return
            
            dfs(root.left)
            count += 1
            if count == k: 
                result = root.val
                return
            dfs(root.right)
            
        dfs(root)
        return result
                