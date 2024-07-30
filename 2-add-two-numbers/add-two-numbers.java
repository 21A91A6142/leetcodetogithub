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
        int sum=0,carry=0;
        ListNode temp1=l1,temp2=l2,head=null,tail=null;
        while(temp1!=null && temp2!=null){
            if(head==null){
                sum=((temp1.val+temp2.val)+carry);
                //System.out.print(sum);
                carry=(sum)/10;
                //System.out.print(carry);
                temp1.val=sum%10;
                head=temp1;
                tail=temp1;
            }
            else{
                sum=((temp1.val+temp2.val)+carry);
                //System.out.print(sum);
                carry=(sum)/10;
                //System.out.print(carry);
                temp1.val=sum%10;
                tail.next=temp1;
                tail=tail.next;
            }
            temp1=temp1.next;
            temp2=temp2.next;
        }
        if(temp1!=null){
            while(temp1!=null){
                sum=((temp1.val)+carry);
                carry=(sum)/10;
                temp1.val=sum%10;
                tail.next=temp1;
                tail=tail.next;
                temp1=temp1.next;
            }
        }
        if(temp2!=null){
            while(temp2!=null){
                sum=((temp2.val)+carry);
                carry=(sum)/10;
                temp2.val=sum%10;
                tail.next=temp2;
                tail=tail.next;
                temp2=temp2.next;
            }
        }
        if(carry>0){
            //System.out.print(carry);
            ListNode newhead=new ListNode(carry,null);
            //System.out.print(tail.next);
            tail.next=newhead;
            tail=tail.next;
        }
        if(tail!=null){
            tail.next=null;
        }
        return head;
    }
}