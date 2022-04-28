# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maxLeft = float('-inf')
        
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def recursiveHelper(root: Optional[TreeNode]) -> bool:
            
            if root.left:
                if root.left.val >= root.val or not self.isValidBST(root.left):
                    return False
                
            if root.val <= self.maxLeft:
                return False
            self.maxLeft = max(self.maxLeft, root.val)

            if root.right:
                if root.right.val <= root.val or not self.isValidBST(root.right):
                    return False
            
            return True
        
        return recursiveHelper(root)