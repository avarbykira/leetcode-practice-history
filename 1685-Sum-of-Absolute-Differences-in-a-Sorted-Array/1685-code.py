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

# brute force
class Solution(object):
    def getSum(self, nums, i, j):
        sum = 0
        for index in range(i, j):
            sum += nums[index]
        return sum
    
    def getSumAbsoluteDifferences(self, nums):
        l = len(nums)
        list = []
        for i in range(0, l):
            dis = (2*i-l)*nums[i] - self.getSum(nums, 0, i) + self.getSum(nums, i, l)
            list.append(dis)
            
        return list
