# Problem Title: 1814. Count Nice Pairs in an Array
# Link: https://leetcode.com/problems/count-nice-pairs-in-an-array/
# Difficulty: Medium

# First Approach: Brute Force
class Solution_First(object):
    def rev(self, num):
        string = str(num)
        string = string[::-1]
        return int(string)
    
    def checkPair(self, num1, num2):
        return (num1 + self.rev(num2)) == (num2 + self.rev(num1))

    def countNicePairs(self, nums):
        count = 0
        length = len(nums)
        for i in range(length):
            for j in range(i+1, length):
                if self.checkPair(nums[i], nums[j]):
                    count += 1

        return count
    
    # Time Limit Exceeded

# Hint 1: The condition can be rearranged to (nums[i] - rev(nums[i])) == (nums[j] - rev(nums[j])).
# Hint 2: Transform each nums[i] into (nums[i] - rev(nums[i])). Then, count the number of (i, j) pairs that have equal values.

# Second Approach
class Solution(object):
    def rev(self, num):
        string = str(num)
        string = string[::-1]
        return int(string)

    def countNicePairs(self, nums):
        numsNew = []
        for num in nums:
            numsNew.append(num - self.rev(num))
        
        count = 0
        length = len(numsNew)
        for i in range(length):
            for j in range(i+1, length):
                if numsNew[i] == numsNew[j]:
                    count += 1
        return count
    