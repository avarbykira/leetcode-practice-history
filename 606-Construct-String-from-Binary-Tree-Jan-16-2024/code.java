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
    public String tree2str(TreeNode root) {
        StringBuilder sb = new StringBuilder();
        if(root == null) return "";
        sb.append(String.valueOf(root.val));
        if(root.left != null) sb.append("(" + tree2str(root.left) + ")");
        if(root.left == null) sb.append("()");
        if(root.right != null) sb.append("(" + tree2str(root.right) + ")");
        if(root.right == null) sb.delete(sb.length()-2, sb.length());
        return sb.toString();
    }
}

class Solution {
    public String tree2str(TreeNode root) {
        StringBuilder sb = new StringBuilder();
        if(root == null) return "";
        sb.append(String.valueOf(root.val));
        sb.append("(" + tree2str(root.left) + ")");
        sb.append("(" + tree2str(root.right) + ")");
        if(sb.length == 5) {
            return sb.subString()
        }
        return sb.toString();
    }
}