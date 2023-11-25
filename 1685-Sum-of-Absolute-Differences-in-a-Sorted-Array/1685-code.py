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
    def getSumAbsoluteDifferences(self, nums):
        l = len(nums)

        # use a list to store sums
        dis = []
        dis.append(0)
        for i in range(0, l-1):
            dis.append(dis[i]+nums[i+1])
        for i in range(0, l-1):
            dis.append(dis[l+i-1]-nums[i])

        list = []
        for i in range(0, l):
            dis = (2*i-l)*nums[i] - self.getSum(nums, 0, i) - dis[i] + self.getSum(nums, i, l) + dis[l+i]
            list.append(dis)
            
        return list
    
# copilot generated
class Solution(object):
    def getSumAbsoluteDifferences(self, nums):
        n = len(nums)
        prefix_sum = [0] * n
        suffix_sum = [0] * n

        # Calculate prefix sum
        prefix_sum[0] = nums[0]
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i-1] + nums[i]

        # Calculate suffix sum
        suffix_sum[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            suffix_sum[i] = suffix_sum[i+1] + nums[i]

        result = []
        for i in range(n):
            result.append((nums[i] * i - prefix_sum[i]) + (suffix_sum[i] - nums[i] * (n-i-1)))

        return result