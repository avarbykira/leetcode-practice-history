// Link: https://leetcode.com/problems/house-robber/description/

// tag: dp

class Solution {
    public int rob(int[] nums) {
        int l = nums.length;

        if (l==1) return nums[l-1];
        if (l==2) return Math.max(nums[l-1], nums[l-2]);

        int[] income = new int[l];
        income[l-1] = nums[l-1];
        income[l-2] = Math.max(nums[l-1], nums[l-2]);

        for (int i=l-3;i>-1;i--) {
            income[i] = Math.max(income[i+1], nums[i]+income[i+2]);
        }
        return income[0];
    }
}