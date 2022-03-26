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
        
        ListNode head = l1;
        ListNode prev = head;
        int remainder = 0;
        while (l1 != null && l2 != null) {
            remainder += l1.val + l2.val;
            l1.val = remainder % 10;
            remainder /= 10;
            prev = l1;
            l1 = l1.next;
            l2 = l2.next;
        }
        if (l2 != null) {
            prev.next = l2;
            l1 = prev.next;
        }
        while (remainder != 0) {
            if (l1 == null) {
                prev.next = new ListNode(remainder);
                break;
            }
            remainder += l1.val;
            l1.val = remainder % 10;
            remainder /= 10;
            prev = l1;
            l1 = l1.next;
        }
        return head;
    }
}