class Solution(object):
    def getSumAbsoluteDifferences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = len(nums)
        disList = []
        for i in range(0, l):
            for j in range(i, l):
                disList.append((i, j, abs(nums[i]-nums[j])))
        
        list = []
        for i in range(0, l):
            dis = 0
            for d in disList:
                if (d[0] == i or d[1] == i):
                    dis += d[2]
            list.append(dis)
        
        return list