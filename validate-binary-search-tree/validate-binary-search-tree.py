# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        result = True
        
        def helper(node: TreeNode) -> tuple[int]:
            nonlocal result
            
            minr = maxr = minl = maxl = None
            
            if result and node.left:
                minl, maxl = helper(node.left)
            if result and node.right:
                minr, maxr = helper(node.right)
            
            if not result:
                return 0, 0
                
            if (minr != None and minr <= node.val) or \
               (maxl != None and maxl >= node.val):
                result = False
            
            return minl if minl != None else node.val, \
             maxr if maxr != None else node.val
        
        helper(root)
        
        return result
            
