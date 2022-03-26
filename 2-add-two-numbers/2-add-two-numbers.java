/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        return recursiveHelper(l1, l2, 0);
    }
    
    private ListNode recursiveHelper(ListNode l1, ListNode l2, int remainder) {
        if (l1 != null && l2 != null) {
            remainder += l1.val + l2.val;
            l1.val = remainder % 10;
            l1.next = recursiveHelper(l1.next, l2.next, remainder/10);
            return l1;
        } else if (l2 != null) {
            return recursiveHelper(l2, l1, remainder);
        } else if (l1 != null) {
            if (remainder != 0) {
                remainder += l1.val;
                l1.val = remainder % 10;
                l1.next = recursiveHelper(l1.next, l2, remainder/10);
            }
            
            return l1;
        } else if (remainder == 0) {
            return null;
        }
        return new ListNode(remainder);
    }
}