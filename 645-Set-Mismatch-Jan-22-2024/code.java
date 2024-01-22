// https://leetcode.com/problems/set-mismatch/description/

class Solution {
    public int[] findErrorNums(int[] nums) {
        

        int[] ans = new int[2];
        for(int i=0;i<nums.length-1;i++) {
            if(nums[i+1]-nums[i] == 0) {
                ans[0] = nums[i];
                break;
            }
        }
        if(ans[0] == 1) {
            ans[1] = 2;
            return ans;
        }
        int missingNum = ans[0]-1;
        for(int i=0;i<nums.length;i++) {
            if(nums[i] == ans[0]-1) {
                missingNum = ans[0]+1;
                break;
            }
        }
        ans[1] = missingNum;
        return ans;
    }
}

class Solution {
    public int[] findErrorNums(int[] nums) {
        int l = nums.length;
        int repeatedNum = -1;
        int missingNum = -1;
        boolean[] memo = new boolean[l+1];
        memo[0] = true;
        for(int i=0;i<l;i++) {
            int n = nums[i];
            if(memo[n] == false) memo[n] = true;
            else repeatedNum = n;
        }
        for(int i=0;i<l+1;i++) {
            if(memo[i] == false) {
                missingNum = i;
                break;
            }
        }
        return new int[]{repeatedNum, missingNum};
    }
}