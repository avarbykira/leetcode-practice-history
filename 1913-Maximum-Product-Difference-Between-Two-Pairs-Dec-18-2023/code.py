class Solution(object):
    def maxProductDifference(self, nums):
        nums.sort()
        return nums[len(nums)-1] * nums[len(nums)-2] - nums[0] * nums[1]
    
# another way
class Solution(object):
    def maxProductDifference(self, nums):
        m1 = max(nums)
        nums.remove(m1)
        m2 = max(nums)
        s1 = min(nums)
        nums.remove(s1)
        s2 = min(nums)
        return m1 * m2 - s1 * s2