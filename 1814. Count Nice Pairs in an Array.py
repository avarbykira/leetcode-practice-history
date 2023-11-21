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
        for num1 in nums:
            for num2 in nums:
                if self.checkPair(num1, num2):
                    count += 1

        return count

