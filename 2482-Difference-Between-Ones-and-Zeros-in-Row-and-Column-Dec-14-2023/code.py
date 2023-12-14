# first commit
class Solution(object):
    def onesMinusZeros(self, grid):
        r, c = len(grid), len(grid[0])
        R = []
        C = []
        for row in grid:
            R.append(row.count(1))
        T = list(zip(*grid))
        for col in T:
            C.append(col.count(1))
        
        mat = [[0 for _ in range(c)] for _ in range(r)]
        for i in range(0, r):
            for j in range(0, c):
                mat[i][j] = 2*(R[i] + C[j]) - r - c
        
        return mat

# modify original matrix
class Solution(object):
    def onesMinusZeros(self, grid):
        r, c = len(grid), len(grid[0])
        R = []
        C = []
        for row in grid:
            R.append(row.count(1))
        T = list(zip(*grid))
        for col in T:
            C.append(col.count(1))
        
        for i in range(0, r):
            for j in range(0, c):
                grid[i][j] = 2*(R[i] + C[j]) - r - c
        
        return grid