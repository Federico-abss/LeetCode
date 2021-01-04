# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        dummy = ListNode()
        node = dummy
        
        while l1 and l2:
            
            if l1.val < l2.val:                
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next               
                            
            node = node.next
            
        node.next = l2 or l1
            
        return dummy.next
                
                
