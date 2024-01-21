// Link: https://leetcode.com/problems/minimum-falling-path-sum/

// tag: matrix, 

// greedy algorithm
class Solution {
    public int minFallingPathSum(int[][] matrix) {
        int sum = 0;
        int index = 0;
        int min = matrix[0][0];
        for(int i=0;i<matrix.length;i++) {
            if(matrix[0][i]<min) {
                min = matrix[0][i];
                index = i;
            }
        }
        sum += min;
        for(int i=1;i<matrix.length;i++) {
            min = matrix[i][index];
            for(int j=index-1;j<=index+1;j++) {
                if(j>0 && j<matrix.length) {
                    if(matrix[i][j]<min) {
                        min = matrix[i][j];
                        index = j;
                    }
                }
            }
            sum += min;
        }
        return sum;
    }
}

// brute force
class Solution {
    public int minFallingPathSum(int[][] matrix) {
        
    }
}