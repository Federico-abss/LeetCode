# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
​
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        path = deque()
        found = False
        def dfs(node):
            nonlocal found
            
            if not found:
                found = node == target
            
            if not node or found:
                return
            
            path.append('L')
            dfs(node.left)
            if found: return
            path.pop()
            path.append('R')
            dfs(node.right)
            if found: return
            path.pop()
            
        
        dfs(original)    
        while path:
            
            if path.popleft() == "R":
                cloned = cloned.right
            else:
                cloned = cloned.left
                
        return cloned
