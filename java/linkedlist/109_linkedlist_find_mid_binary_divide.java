/**

typical two pointer for linkedlist to find mid


 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public TreeNode sortedListToBST(ListNode head) {
        if(head == null){
            return null;
        }
        
        // find mid
        ListNode slow = head;
        ListNode fast = head;
        // to break the connection between slow and slowPre
        ListNode slowPre = null;
        
        while(fast.next != null && fast.next.next != null){
            slowPre = slow;
            slow = slow.next;
            fast = fast.next.next;
        }
        
        // root is the slow val
        TreeNode root = new TreeNode(slow.val);
        
        // break connection
        if(slowPre != null){
            slowPre.next = null;    
        }
        
        if(slow != head){
            root.left = sortedListToBST(head);
        }
        
        root.right = sortedListToBST(slow.next);
        
        return root;
    }
}