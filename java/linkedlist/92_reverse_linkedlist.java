/**

super important
linkedlist reverse
need to practice more

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
    public ListNode reverseBetween(ListNode head, int left, int right) {
        if(head.next == null){
            return head;
        }
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode beforeReversed = null;
        ListNode afterReversed = null;
        ListNode detect = dummy;
        for(int i = 0; i < right; i++){
            
            if(i == left - 1){
                beforeReversed = detect;
            }
            detect = detect.next;
        }
        
        
        beforeReversed.next = reverseN(beforeReversed.next, right-left+1);
        
        return dummy.next;
        
    }
    

    
    private static ListNode reverseN(ListNode head, int n){
        if(n == 1){
            return head;
        }
        
        ListNode nextOfLast = head;
        ListNode newLast = head;
        ListNode newHeadOfReversedPart = null;
        for(int i = 1; i <= n; i++){
            //if(i == n - 1)
            nextOfLast = nextOfLast.next;
            if(i == n - 1){
                newHeadOfReversedPart = nextOfLast;
            }
        }
        
        //ListNode newHead = recurReverse(head, n);
    recurReverse(head, n);
        
        newLast.next = nextOfLast;
        
        return newHeadOfReversedPart;    
        
        
    }
    
    private static ListNode recurReverse(ListNode head, int n){
        if(n == 1){
            return head;
        }
        
        recurReverse(head.next, n - 1).next = head;
        
        return head;
    }
}