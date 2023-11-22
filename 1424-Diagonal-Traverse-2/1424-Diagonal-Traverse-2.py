class Solution(object):
    def findDiagonalOrder(self, nums):
        # use a new list to represent a full matrix
        # store -1 to empty cells
        numsLen = len(nums)
        listNew = []
        for list in nums:
            innerList = [None] * numsLen
            i = 0
            for num in list:
                innerList[i] = num
                i += 1
            for j in range(i, numsLen):
                innerList[j] = -1
            listNew.append(innerList)
        
        # add them to a new list by order
        listFinal = []
        for turn in range(0, (len(nums)-1)*2):
            for y in range(0, turn):
                x = turn - y
                if x<len(nums) and y<len(nums):
                    listFinal.append(listNew[x][y])
        
        # delete all -1
        while -1 in listFinal:
            listFinal.remove(-1)