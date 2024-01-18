// Link: https://leetcode.com/problems/climbing-stairs/description/

// these types of question has a similar pattern: 
// if you wanna solve the ultimate problem, you can solve the downgraded one first.

class Solution {
    public int climbStairs(int n) {
        if(n==1) return 1;
        if(n==2) return 2;
        return 2*climbStairs(n-2);
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