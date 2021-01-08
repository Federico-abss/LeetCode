"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
​
class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        result = ""
        if not root:
            return result
        
        dq = deque([root, None])
        while dq:
            
            cur = dq.popleft()
            
            if not cur:
                result += "#"
                
            else:
                result += str(cur.val) 
                if dq[0] != None:
                    result += ','
                
                for child in cur.children:
                    dq.append(child)
                dq.append(None)
        
        return result
    
        
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if not data:
            return
        nodes = deque(data.split('#'))
        root = Node(int(nodes.popleft()), [])
        dq = deque([root])
        
        while dq:
            
            cur = dq.popleft()
            
            children = nodes.popleft().split(',')
            for child in children:
                if not child:
                    continue
                node = Node(int(child), [])
                cur.children.append(node)
                dq.append(node)
                
        return root
        
        
​
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
