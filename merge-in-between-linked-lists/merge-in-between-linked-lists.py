# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        
        node = list1
        count = 1
        while count != a:
            count += 1
            node = node.next
            
        cut = node.next
        node.next = list2
        
        while list2.next:
            list2 = list2.next
            
        while count != b:
            count += 1
            cut = cut.next
            
        list2.next = cut.next
        
        return list1
            
