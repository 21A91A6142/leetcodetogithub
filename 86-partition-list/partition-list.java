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
    public ListNode partition(ListNode head, int x) {
        ListNode gh=null,gt=null,lh=null,lt=null;
        ListNode temp=head;
        while(temp!=null){
            if(temp.val<x){
                if(lh==null){
                    lh=temp;
                    lt=temp;
                }
                else{
                    lt.next=temp;
                    lt=lt.next;
                }
            }
            else{
                if(gh==null){
                    gh=temp;
                    gt=temp;
                }
                else{
                    gt.next=temp;
                    gt=gt.next;
                }
            }
            temp=temp.next;
        }
        if(gt!=null){
            gt.next=null;
        }
        if(lh==null && gh!=null){
            return gh;
        }
        if(gh==null && lh!=null){
            if(lt!=null){
                lt.next=null;
            }
            return lh;
        }
        if(lh!=null && gh!=null){
            lt.next=gh;
            return lh;
        }
        return null;
    }
}