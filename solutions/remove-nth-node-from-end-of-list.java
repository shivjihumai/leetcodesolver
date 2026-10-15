/**
 * Problem: Remove Nth Node From End of List (Medium)
 * Language: Java
 *
 * Description:
 * Given the `head` of a linked list, remove the `nth` node from the end of the list and return its head.
 * 
 *  
 * 
 * **Example 1:**
 * 
 * **Input:** head = [1,2,3,4,5], n = 2
 * **Output:** [1,2,3,5]
 * 
 * **Example 2:**
 * 
 * **Input:** head = [1], n = 1
 * **Output:** []
 * 
 * **Example 3:**
 * 
 * **Input:** head = [1,2], n = 1
 * **Output:** [1]
 * 
 *  
 * 
 * **Constraints:**
 * 
 * 	• The number of nodes in the list is `sz`.
 * 
 * 	• `1 <= sz <= 30`
 * 
 * 	• `0 <= Node.val <= 100`
 * 
 * 	• `1 <= n <= sz`
 * 
 *  
 * 
 * **Follow up:** Could you do this in one pass?
 */

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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        // Create a dummy node to handle edge cases where the head is removed
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        
        ListNode fast = dummy;
        ListNode slow = dummy;
        
        // Move fast pointer n steps ahead
        for (int i = 0; i < n; i++) {
            fast = fast.next;
        }
        
        // Move both pointers until fast reaches the end (null)
        // At this point, slow will be at the node before the one to be removed
        while (fast.next != null) {
            fast = fast.next;
            slow = slow.next;
        }
        
        // Remove the nth node from the end
        slow.next = slow.next.next;
        
        return dummy.next;
    }
}
