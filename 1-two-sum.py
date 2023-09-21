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

        # find the length of the bool array
        biggestNum = 0
        for num in nums:
            if num > biggestNum:
                biggestNum = num

        # initialize a bool array
        boolArray = [False] * (biggestNum+1)
        for num in nums:
            boolArray[num] = True

        # iterate for 'nums' list
        i = 0
        while i < len(nums):
            if boolArray[target - nums[i]]:
                break
            i += 1

        j = 0
        while j < len(nums):
            if nums[j] == target - nums[i]:
                break
            j += 1

        return i, j



        # initial attempt: Time Limit Exceeded
        #
        # i, j = 0, 0
        #
        # while i < len(nums):
        #     while j < len(nums):
        #         j = i
        #         if nums[i] + nums[j] == target:
        #             return i, j
        #         j += 1
        # i += 1
