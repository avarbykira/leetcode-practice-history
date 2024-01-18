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