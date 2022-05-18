"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return
        
        q = deque()
        q.append(node)
        
        seen = dict()
        copy = Node(node.val)
        seen[node] = copy
        
        while q:
            cur = q.popleft()
            curCopy = seen[cur]
            for neighbor in cur.neighbors:
                if neighbor not in seen:
                    seen[neighbor] = Node(neighbor.val)
                    q.append(neighbor)
                curCopy.neighbors.append(seen[neighbor])
            
        return copy
        
                    
                    
                    
                
                    