// Link: https://leetcode.com/problems/climbing-stairs/description/

// these types of question has a similar pattern: 
// if you wanna solve the ultimate problem, you can solve the downgraded one first.

// tag: recursion, TLE

class Solution {
    public int climbStairs(int n) {
        if(n<=0) return 0;
        if(n==1) return 1;
        if(n==2) return 2;
        return climbStairs(n-1) + climbStairs(n-2);
    }
}

class Solution {
    public int climbStairs(int n) {
        int count = 1;
        for(int i=1;i<=n/2;i++) {
            int a = n-i*2;
            count += a*(a+1)/2;
        }
        return count;
    }
}

class Solution {
    public int climbStairs(int n) {
        if (n <= 0) return 0;
        if (n == 1) return 1;
        if (n == 2) return 2;
        
        int[] dp = new int[n + 1];
        dp[1] = 1;
        dp[2] = 2;
        
        for (int i = 3; i <= n; i++) {
            dp[i] = dp[i - 1] + dp[i - 2];
        }
        
        return dp[n];
    }
}