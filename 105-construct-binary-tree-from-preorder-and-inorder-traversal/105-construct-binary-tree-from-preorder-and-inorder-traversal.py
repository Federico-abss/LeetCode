# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        
        root = TreeNode(preorder[0])
        idxRoot = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:idxRoot+1], inorder[:idxRoot])
        root.right = self.buildTree(preorder[idxRoot+1:], inorder[idxRoot+1:])
        
        return root
        
        
        