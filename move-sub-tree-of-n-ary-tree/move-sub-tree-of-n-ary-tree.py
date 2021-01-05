"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""
​
class Solution:
    def moveSubTree(self, root: 'Node', p: 'Node', q: 'Node') -> 'Node':
   
        if p in q.children:
            
            return root    
        
        parentP = parentQ = None
        
        dq = deque([root])
        
        while dq and not (parentP and parentQ):
            
            cur = dq.popleft()
            
            dq.extend(cur.children)
            
            if q in cur.children:
                parentQ = cur
            if p in cur.children:
                parentP = cur
                
        stack = [p]
        isQChild = False
        while parentP and stack and not isQChild:
            
            cur = stack.pop()
            
            stack += cur.children
            if q in cur.children:
                isQChild = True
        
        if isQChild and parentP:
            
            index = parentP.children.index(p)
            parentP.children.pop(index)
            parentQ.children.pop(parentQ.children.index(q))
            
            parentP.children.insert(index, q)
            q.children.append(p)
            
        elif not parentP:
            
            parentQ.children.pop(parentQ.children.index(q))
            root = q 
            q.children.append(p)
            
        else:
            
            parentP.children.pop(parentP.children.index(p))
            q.children.append(p)
                
        return root
        
