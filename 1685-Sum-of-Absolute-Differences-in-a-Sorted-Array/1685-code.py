class Solution(object):
    def getSumAbsoluteDifferences(self, nums):
        l = len(nums)
        disList = []
        for i in range(0, l):
            for j in range(i, l):
                disList.append((i, j, nums[j]-nums[i])) # since nums is non-decresing
        
        list = []
        for i in range(0, l):
            dis = 0
            for d in disList:
                if (d[0] == i or d[1] == i):
                    dis += d[2]
            list.append(dis)
        
        return list
    
    class Solution(object):
        def getSumAbsoluteDifferences(self, nums):
            l = len(nums)
            list = []
            for i in range(0, l):
                dis = 0
                for j in range(0, l):
                    if i<j:
                        dis += nums[j] - nums[i]
                    else:
                        dis += nums[i] - nums[j]
                list.append(dis)
                
            return list
