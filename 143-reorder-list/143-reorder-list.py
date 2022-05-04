# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """  
        stack = []
        cur = head
        while cur:
            stack.append(cur)
            cur = cur.next
            
        lenList = len(stack)
        while len(stack) > ceil(lenList / 2):
            node = stack.pop()
            stack[-1].next = None
            nextNode = head.next
            head.next = node
            node.next = nextNode
            head = nextNode
    
            