class Solution(object):
    def numSpecial(self, mat):
        r, c = len(mat), len(mat[0])
        singleElementRow = []
        singleElementCol = []
        for i in range(0, r):
            row = mat[i]
            row.sort()
            if row[c-1] == 1 and row[c-2] == 0:
                singleElementRow.append(i)
        for j in range(0, c):
            column = []
            for row in mat:
                column.append(row[j])
            column.sort()
            if column[r-1] == 1 and column[r-2] == 0:
                singleElementCol.append(j)
        for 

class Solution(object):
    def check(self, mat, mat_T, i, j, r, c):
        row = mat[i]
        col = mat_T[j]
        row.sort()
        col.sort()
        return row[c-1] == 1 and row[c-2] == 0 and col[r-1] == 1 and col[r-2] == 0
        
    def numSpecial(self, mat):
        count = 0
        r, c = len(mat), len(mat[0])
        mat_T = []
        for j in range(0, c):
            column = []
            for row in mat:
                column.append(row[j])
                mat_T.append(column)
        
        points = []
        for i in range(0, r):
            for j in range(0, c):
                if mat[i][j] == 1:
                    point = (i, j)
                    if self.check(mat, mat_T, i, j, r, c) and point not in points:
                        count += 1
                        points.append(point)
                        
        
        return count
    
class Solution(object):
    def numSpecial(self, mat):
        r, c = len(mat), len(mat[0])
        points = []
        mat_T = [[0 for _ in range(r)] for _ in range(c)]
        for i in range(0, r):
            for j in range(0, c):
                mat_T[j][i] = mat[i][j]
                if mat[i][j] == 1:
                    points.append((i, j))
        
        count = 0
        for point in points:
            i, j = point[0], point[1]
            countR, countC = 0
            for n in mat[i]:
                if n == 1:
                    countR += 1
            for n in mat_T[j]:
                if n == 1:
                    countC += 1
            if countR == countC == 1:
                count += 1
        
        return count