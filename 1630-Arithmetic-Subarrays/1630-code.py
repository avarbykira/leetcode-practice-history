class Solution(object):
    """
    check whether a list is Arithmetic. List should:
        1. ascend ordered
        2. has at least 2 elements in it
    """
    def isArithmetic(self, nums):
        diff = nums[1] - nums[0]
        for i in range(0, len(nums)-1):
            if nums[i+1] - nums[i] != diff:
                return False
            else:
                return True


    def checkArithmeticSubarrays(self, nums, l, r):
        record = []

        # len(l) == len(r), given by problem

        for i in range(0, len(l)):
            if r[i] - l[i] == 1:
                record.append(False)
            else:
                subarray = nums[l[i]:r[i]+1]
                subarray.sort()
                record.append(self.isArithmetic(subarray))
    
        return record
                