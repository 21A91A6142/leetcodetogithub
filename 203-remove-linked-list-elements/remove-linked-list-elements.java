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
    public ListNode removeElements(ListNode head, int val) {
        if(head==null){
            return head;
        }
        ListNode head1=null,tail=null,temp=head;
        while(temp!=null){
            if(head1==null && temp.val!=val){
                head1=temp;
                tail=temp;
                temp=temp.next;
            }
            else{
                if(temp.val==val){
                    temp=temp.next;
                }
                else{
                    tail.next=temp;
                    tail=tail.next;
                    temp=temp.next;
                }
            }
        }
        if(tail!=null){
            tail.next=null;
        }
        return head1;
        
    }
}