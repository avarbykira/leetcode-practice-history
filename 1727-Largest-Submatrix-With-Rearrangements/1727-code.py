class Solution(object):
    def largestSubmatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        
        # rearrange the list to column first
        row = len(matrix)
        col = len(matrix[0])
        newMatrix = []
        counter = []

        for i in range(0, col):
            count = 0
            column = []
            for list in matrix:
                column.append(list[i])
                if list[i] == 1:
                    count += 1
            counter.append((i, count))
            newMatrix.append(column)
        
        # reorder the newMatrix
        counter.sort(key=lambda x: x[1])
        M = []
        for c in counter:
            M.append(newMatrix[c[0]])
        
        # find the largest square of 1s
        
        
                