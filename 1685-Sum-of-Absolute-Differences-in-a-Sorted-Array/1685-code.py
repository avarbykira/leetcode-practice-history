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
                disList.append(abs(nums[i]-nums[j]))
        
        list = []
        for i in range(0, l):
            dis = 0
            for j in range(0, l):
                dis += disList[i*l - i*(i-1)/2 + j]
            list.append(dis)
        
        return list