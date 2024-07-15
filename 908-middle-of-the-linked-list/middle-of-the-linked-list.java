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
    public ListNode middleNode(ListNode head) {
        int c=0,k=0;
        ListNode temp=head;
        while(temp!=null){
            c++;
            temp=temp.next;
        }
        temp=head;
        while(temp!=null){
            if(k==c/2){
                break;
            }
            k++;
            temp=temp.next;
        }
        return temp;

    }
}