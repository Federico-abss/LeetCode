# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        
        lists = []
        
        cur = head
        while cur:
            lists.append(cur)
            cur = cur.next
            lists[-1].next = None

                
        def conquer(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
            
            if len(lists) == 1:
                return lists[0]
            
            elif len(lists) == 2:
                n1 = lists[0]
                n2 = lists[1]
                head = ListNode()
                cur = head
                
                while n1 and n2:
                    if n1.val <= n2.val:
                        cur.next = n1
                        n1 = n1.next
                        
                    else:
                        cur.next = n2
                        n2 = n2.next
                        
                    cur = cur.next
                    
                if n1:
                    cur.next = n1
                else:
                    cur.next = n2
                    
                return head.next
            
            else:
                return conquer([conquer(lists[:len(lists)//2]), conquer(lists[len(lists)//2:])])
            
        return conquer(lists)
                
            
                    