"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def __init__(self):
        self.seen = dict()
        
        
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return
        
        copy = Node(node.val)
        self.seen[node] = copy
    
        for neighbor in node.neighbors:
            if neighbor not in self.seen:
                self.seen[neighbor] = self.cloneGraph(neighbor)
            copy.neighbors.append(self.seen[neighbor])   
            
        return copy
        
                    
                    
                    
                
                    