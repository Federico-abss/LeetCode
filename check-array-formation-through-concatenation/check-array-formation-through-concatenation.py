# single node of a linked list
class ListNode:
    def __init__(self, val = 0, next = None):
        
        self.val = val
        self.next = next
        
​
class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        
        dummy = ListNode()
        cur = dummy
        hmap = {}
        # construct a linked list out of arr
        # and store the nodes in hashmap 
        for num in arr:
            
            cur.next = ListNode(num)             
            cur = cur.next 
            hmap[num] = cur             
        
        for piece in pieces:
            
            cur = None
            tail = False
            for num in piece:
                # if we have a node we follow the list and check if 
                # each node value matches with the current piece
                # otherwise search the hmap to find the node
                if ((not cur and num in hmap) or (cur and num == cur.val)) and not tail:
                    cur = hmap[num]
                    cur = cur.next
                    if not cur:
                        tail = True
                
                # if the hmap does not contain the num or the
                # next values in the piece do not correspond to
                # the continuation of the list we return false
                else:
                    return False
            
        return True
