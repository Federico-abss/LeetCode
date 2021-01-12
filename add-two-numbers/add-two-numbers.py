# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        def numFromList(node):
            
            result = 0
            i = 0
            
            while node:
                
                result += node.val * 10 ** i
                node = node.next
                i += 1
                
            return result
        
        
        number = numFromList(l1) + numFromList(l2)
        
        dummy = ListNode(0)
        node = dummy
        for ch in reversed(str(number)):
            
            node.next = ListNode(int(ch))
            node = node.next
            
        return dummy.next
            
            
