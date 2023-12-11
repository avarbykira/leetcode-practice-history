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

        StringBuilder sb = new StringBuilder();

        sb.append(l1.val.toString());
        while(l1.next != null) {
            sb.append(l1.next.val.toString());
        }

        int num1 = Integer.parseInt(sb.reverse().toString());

        sb.setLength(0);

        sb.append(l2.val.toString());
        while(l1.next != null) {
            sb.append(l2.next.val.toString());
        }

        int num2 = Integer.parseInt(sb.reverse().toString());

        int outcome = num1 + num2;

        sb.setLength(0);

        sb.append(outcome);
        ListNode lastNode = new ListNode(Integer.parseInt(String.valueOf(sb.toString().charAt(0))));
        for(int i=1; i<sb.length(); i++) {
            ListNode ls = new ListNode(Integer.parseInt(Integer.parseInt(String.valueOf(sb.toString().charAt(i))), lastNode));
            lastNode = ls;
        }

        return lastNode;
        
    }
}