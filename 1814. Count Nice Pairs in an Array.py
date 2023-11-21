class Solution(object):
    def rev(self, num):
        string = str(num)
        string = string[::-1]
        return int(string)
    
    def checkPair(self, num1, num2):
        return (num1 + self.rev(num2)) == (num2 + self.rev(num1))

    def countNicePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        count = 0
        length = len(nums)
        for i in range(length):
            for j in range(i, length):
                if self.checkPair(nums[i], nums[j]):
                    count += 1
        return count

