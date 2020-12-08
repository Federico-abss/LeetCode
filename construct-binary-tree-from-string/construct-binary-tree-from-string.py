# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> TreeNode:
        
        if not s:
            return
        
        start = 1
        while start < len(s) and s[start] != "(":
            start += 1
        
        node = TreeNode(int(s[0:start]))
            
        if start < len(s) and s[start] == "(":
            start += 1
            idx = start
            stack = 1
            while stack:
                    
                idx += 1
                if s[idx] == "(":
                    stack += 1
                elif s[idx] == ")":
                    stack -= 1
​
            node.left = self.str2tree(s[start:idx])
                
            if len(s) > idx + 1:
                node.right = self.str2tree(s[idx + 2:-1])
            
        return node
        
