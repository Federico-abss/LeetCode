class ListNode:
    def __init__(self, val = 0, next = None):
        
        self.val = val
        self.next = next
        
​
class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        
        tot = 0
        dummy = ListNode()
        cur = dummy
        for num in arr:
            
            cur.next = ListNode(num)
            cur = cur.next
            
        hmap = {}
        
        cur = dummy.next
        while cur:
            
            hmap[cur.val] = cur
            cur = cur.next
        
        for piece in pieces:
            
            cur = None
            tail = False
            for num in piece:
                if ((not cur and num in hmap) or (cur and num == cur.val)) and not tail:
                    cur = hmap[num]
                    tot += 1
                    cur = cur.next
                    if not cur:
                        tail = True
                        
                else:
                    return False
            
        
        return True
