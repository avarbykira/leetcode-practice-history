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
        boolArray = [False] * (biggestNum + 1)
        count = [0] * (biggestNum + 1)

        for num in nums:
            boolArray[num] = True
            count[num] += 1

        # iterate for 'nums' list
        i = 0
        while i < len(nums):
            if boolArray[target - nums[i]]:
                if target - nums[i] == nums[i]:
                    if count[nums[i]] == 2:
                        break
                    else:
                        continue
                else:
                    break
            i += 1

        j = 0
        while j < len(nums):
            if nums[j] == target - nums[i] and j != i:
                break
            j += 1

        return i, j
