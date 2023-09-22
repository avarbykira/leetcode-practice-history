"""
Date: 22/09/2023

Problem Link: https://leetcode.com/problems/median-of-two-sorted-arrays/
"""


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        mid = int(len(nums1) + len(nums2)) + 1

        i, j = 0, 0
        count = 0
        flag = False

        while count < mid:
            if nums1[i] < nums2[j]:
                i += 1
                count += 1
                flag = True
            else:
                j += 1
                count += 1
                flag = False

        if (len(nums1) + len(nums2)) % 2 != 0:
            if flag:
                return nums1[i]
            else:
                return nums2[j]
        else:
            if flag:
                return nums[i]



        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
