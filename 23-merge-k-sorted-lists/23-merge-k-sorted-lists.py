# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        q = []
        setattr(ListNode, "__lt__", lambda self, other: self.val <= other.val)
        
        for list in lists:
            if list:
                heappush(q, list)
            
        head = ListNode()
        cur = head
        
        while q:
            node = heappop(q)
            cur.next = node
            if node.next:
                heappush(q, node.next)
            cur = cur.next
            
            
        return head.next