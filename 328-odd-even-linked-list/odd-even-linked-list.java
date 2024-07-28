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
    public ListNode oddEvenList(ListNode head) {
        ListNode oih=null,oit=null,eih=null,eit=null,temp=head;
        int k=1;
        while(temp!=null){
            if(k%2!=0){
                if(oih==null){
                    oih=temp;
                    oit=temp;
                    k++;
                }
                else{
                    oit.next=temp;
                    oit=oit.next;
                    k++;
                }
            }
            else{
                if(eih==null){
                    eih=temp;
                    eit=temp;
                    k++;
                }
                else{
                    eit.next=temp;
                    eit=eit.next;
                    k++;
                }
            }
            temp=temp.next;
        }
        if(eit!=null){
            eit.next=null;
        }
        if(oih!=null && eih==null){
            oit.next=null;
            return oih;
        }
        if(oih==null && eih!=null){
            return eih;
        }
        if(oih!=null && eih!=null){
            oit.next=eih;
            return oih;
        }
        return null;
    }
}