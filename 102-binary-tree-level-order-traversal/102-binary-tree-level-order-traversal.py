# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        q = deque([root, None])
        result = [[]]
        
        while q:
            node = q.popleft()
            if not node:
                if not q: 
                    break
                q.append(None)
                result.append([])
                continue
                
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            
            result[-1].append(node.val)
            
        return result
            