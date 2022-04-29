# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        q = deque([root, None])
        result = [[]]
        
        while len(q) > 1:
            cur = q.popleft()
            if not cur:
                result.append([])
                q.append(None)
                continue
                
            result[-1].append(cur.val)
            
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
                
                    
        realResult = []
        zag = False
        for res in result:
            if zag:
                realResult.append(res[::-1])
            else:
                realResult.append(res)
            zag = not zag
            
        return realResult
            
            