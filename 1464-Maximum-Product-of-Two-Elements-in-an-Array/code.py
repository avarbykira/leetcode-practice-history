class Solution(object):
    def maxProduct(self, nums):
        nums.sort()

        l = len(nums)

        return (nums[l-1]-1) * (nums[l-2]-1)