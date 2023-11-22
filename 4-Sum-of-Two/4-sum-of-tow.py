"""
Date: 22/09/2023

Problem Link: https://leetcode.com/problems/median-of-two-sorted-arrays/
"""


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):

        flag = False
        if (len(nums1) + len(nums2)) % 2 == 0:
            flag = True

        length = int((len(nums1) + len(nums2)) / 2) + 1

        count = mid = midBefore = i = j = 0

        while count < length:
            midBefore = mid
            if nums1[i] < nums2[j]:
                mid = nums1[i]
                j += 1
            else:
                mid = nums2[j]
                i += 1
            count += 1

        if flag:
            return (mid+midBefore) / 2
        else:
            return mid


        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
