class Solution(object):
    def findDiagonalOrder(self, nums):
        # use a new list to represent a full matrix
        # store -1 to empty cells

        # decide the dimention of new matrix
        dim = len(nums)
        for list in nums:
            if len(list) > dim:
                dim = len(list)

        listNew = [[-1 for _ in range(dim)] for _ in range(dim)]

        i = 0
        for list in nums:
            j = 0
            for num in list:
                listNew[i][j] = num
                j += 1
            i+= 1
        
        # add them to a new list by order
        listFinal = []
        for turn in range(0, 2*dim-1):
            for y in range(0, turn+1):
                x = turn - y
                if x<dim and y<dim:
                    listFinal.append(listNew[x][y])
        
        # delete all -1
        while -1 in listFinal:
            listFinal.remove(-1)

        return listFinal