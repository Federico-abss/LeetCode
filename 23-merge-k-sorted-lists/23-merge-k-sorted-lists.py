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


def partition(lists: List[Optional[ListNode]], start: int, end: int) -> ListNode:
    if start == end: 
        return lists[start]
    
    mid = (end + start) // 2
    l1 = partition(lists, start, mid)
    l2 = partition(lists, mid+1, end)
    return mergeTwoLists(l1, l2)
    

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        return partition(lists, 0, len(lists) - 1)
        
        
    
    
    