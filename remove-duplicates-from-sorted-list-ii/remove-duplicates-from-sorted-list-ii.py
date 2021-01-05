# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        dummy = ListNode(0, head)
        node = head
        prev = dummy
        
        while node and node.next:
            
            if node.next.val == node.val:
                while node.next and node.next.val == node.val:                
                    node.next = node.next.next
​
                prev.next = node.next
                node = prev
            
            prev, node = node, node.next
            
        return dummy.next
