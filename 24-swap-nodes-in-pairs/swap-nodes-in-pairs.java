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
    public ListNode swapPairs(ListNode head) {
        if(head==null || head.next==null){
            return head;
        }
        ListNode temp=head;
        int k=0;
        while(temp.next!=null){
            if(k%2==0){
                System.out.print(k);
                int tem=temp.val;
                temp.val=temp.next.val;
                temp.next.val=tem;
            }
            k++;
            temp=temp.next;
        }
        return head;
    }
}