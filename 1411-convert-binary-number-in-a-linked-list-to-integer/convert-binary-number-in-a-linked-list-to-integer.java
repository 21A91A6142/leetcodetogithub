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
    /*public static ListNode reverse(ListNode head){
        if(head.next==null){
            return head;
        }
        ListNode small=reverse(head.next);
        small.next=head;
        head.next=null;
        return small;
    }*/
    public int getDecimalValue(ListNode head) {
        if(head==null){
            return 0;
        }
        //ListNode k=reverse(head);
        ListNode temp=head;
        int k1=0,p=0;
        while(temp!=null){
            k1+=1;
            temp=temp.next;
        }
        temp=head;
        while(temp!=null){
            p+=(temp.val)*Math.pow(2,k1-1);
            k1--;
            temp=temp.next;
        }
        return p;
    }
}