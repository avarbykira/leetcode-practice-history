"""
Date: 21/09/2023

Brief Problem Description:
Initial thoughts or approach to the problem:
Problem Link:

Time complexity:
Space complexity:
"""

"""
:type nums: List[int]
:type target: int
:rtype: List[int]
"""


class Solution(object):
    def twoSum(self, nums, target):

        i, j = 0

        while i < len(nums):
            while j < len(nums):
                j = i
                if nums[i] + nums[j] == target:
                    return i, j
                j += 1
        i += 1
