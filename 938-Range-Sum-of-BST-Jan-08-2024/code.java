import java.util.ArrayList;

/**
 * Link: https://leetcode.com/problems/range-sum-of-bst/
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

public class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {
    public int rangeSumBST(TreeNode root, int low, int high) {
        ArrayList<TreeNode> l = new ArrayList<>();
        int sum = 0;
        l.add(root);
        while(!l.isEmpty()) {
            TreeNode n = l.remove(0);
            if(n.left != null) {
                l.add(n.left);
            }
            if(n.right != null) {
                l.add(n.right);
            }
            if(n.val <= high && n.val >= low){
                sum += n.val;
            }
        }
        return sum;
        
    }
}

class Solution {
    public int rangeSumBST(TreeNode root, int low, int high) {
        int sum = 0;
        if(root == null) return 0;
        if(root.val<=high && root.val>=low){
            sum += root.val;
        }
        sum += rangeSumBST(root.left, low, high);
        sum += rangeSumBST(root.right, low, high);
        return sum;
    }
}