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

        for i in range(0, col):
            column = []
            for list in matrix:
                column.append(list[i])
            newMatrix.append(column)
        
        # calculate consecutive ones
        for column in newMatrix:
            count = 0
            i, j = 0
            for index in range(0, col):
                if column[index] == 


        
        
                