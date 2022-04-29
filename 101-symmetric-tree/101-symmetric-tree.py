# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        
        def recursive(root: Optional[TreeNode], nodes: List[List[TreeNode]], level: int) -> List[List[TreeNode]]:
            if level >= len(nodes):
                nodes.append([])
                
            nodes[level].append(root.val if root else None)
                
            if not root:
                return [[None]]
            
            recursive(root.left, nodes, level+1)
            recursive(root.right, nodes, level+1)
            
            return nodes
        
        return recursive(root.left, [], 0) == list(map(lambda x: list(reversed(x)), recursive(root.right, [], 0)))
                
            