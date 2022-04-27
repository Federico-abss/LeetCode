# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if not root: return result
        
        stack = []
        while root:
            stack.append(root)
            root = root.left
        
        while stack: 
            cur = stack.pop()
            result.append(cur.val)
            
            if cur.right:
                cur = cur.right
                stack.append(cur)
                while cur.left:
                    cur = cur.left
                    stack.append(cur)
        
            
        return result
            
        
        