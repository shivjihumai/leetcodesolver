/**
 * Problem: Reverse Nodes in k-Group (Hard)
 * Language: Java
 *
 * Description:
 * Given the `head` of a linked list, reverse the nodes of the list `k` at a time, and return *the modified list*.
 * 
 * `k` is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of `k` then left-out nodes, in the end, should remain as it is.
 * 
 * You may not alter the values in the list's nodes, only nodes themselves may be changed.
 * 
 *  
 * 
 * **Example 1:**
 * 
 * **Input:** head = [1,2,3,4,5], k = 2
 * **Output:** [2,1,4,3,5]
 * 
 * **Example 2:**
 * 
 * **Input:** head = [1,2,3,4,5], k = 3
 * **Output:** [3,2,1,4,5]
 * 
 *  
 * 
 * **Constraints:**
 * 
 * 	• The number of nodes in the list is `n`.
 * 
 * 	• `1 <= k <= n <= 5000`
 * 
 * 	• `0 <= Node.val <= 1000`
 * 
 *  
 * 
 * **Follow-up:** Can you solve the problem in `O(1)` extra memory space?
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
    public ListNode reverseKGroup(ListNode head, int k) {
        if (head == null || k <= 1) {
            return head;
        }

        ListNode dummy = new ListNode(0);
        dummy.next = head;
        
        ListNode prevGroupEnd = dummy;
        ListNode curr = head;

        while (true) {
            // Check if there are at least k nodes remaining
            ListNode kthNode = prevGroupEnd;
            for (int i = 0; i < k; i++) {
                kthNode = kthNode.next;
                if (kthNode == null) {
                    // Not enough nodes left, return the result
                    return dummy.next;
                }
            }
            
            // kthNode is the k-th node from prevGroupEnd
            // The next group starts after kthNode
            ListNode nextGroupStart = kthNode.next;
            
            // Reverse the k nodes starting from curr
            // curr is the head of the current group
            // kthNode is the tail of the current group (before reversal)
            // After reversal, kthNode becomes the head, and curr becomes the tail
            
            ListNode prev = nextGroupStart;
            ListNode node = curr;
            while (node != nextGroupStart) {
                ListNode nextTemp = node.next;
                node.next = prev;
                prev = node;
                node = nextTemp;
            }
            
            // Now, prev is the new head of the reversed group (which was kthNode)
            // curr is the new tail of the reversed group
            
            // Connect the previous group's end to the new head
            prevGroupEnd.next = prev;
            
            // Move prevGroupEnd to the new tail (which is curr)
            prevGroupEnd = curr;
            
            // Move curr to the start of the next group
            curr = nextGroupStart;
        }
    }
}
