# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

setattr(ListNode, "__lt__", lambda self, other: self.val <= other.val)

def mergeTwoLists(l1: ListNode, l2: ListNode):
    
    if not l1: 
        return l2
    if not l2:
        return l1
    
    head = ListNode()
    cur = head
    
    while l1 and l2:
        if l1 < l2:
            cur.next = l1
            cur = cur.next
            l1 = l1.next
        else:
            cur.next = l2
            cur = cur.next
            l2 = l2.next
            
    if l1:
        cur.next = l1
    else:
        cur.next = l2 
            
    return head.next
    

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        lists2 = []
        
        if not lists:
            return
        
        while len(lists2) > 1 or len(lists) > 1:
            while len(lists) > 1:
                lists2.append(mergeTwoLists(lists.pop(), lists.pop()))
                
            while len(lists2) > 1:
                lists.append(mergeTwoLists(lists2.pop(), lists2.pop()))
                
        
        return mergeTwoLists(lists[0] if lists else None, lists2[0] if lists2 else None)
        
        
    
    
    