# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        
        mDepth = 0
        floors = []
        
        def helper(node, depth):
            nonlocal mDepth, floors
            
            if not node:
                if mDepth < depth - 1:
                    floors = []
                    mDepth = depth - 1
                while len(floors) <= mDepth:
                    floors.append([])
                return depth - 1
            
            l = helper(node.left, depth + 1)
            r = helper(node.right, depth + 1)
            
            maxDepth = max(l, r)          
            if mDepth == maxDepth:
                floors[depth].append(node)
            
            return maxDepth
        
        helper(root, 0)
        while len(floors[-1]) != 1:
            floors.pop()
            
        return floors[-1][0]
        
        
