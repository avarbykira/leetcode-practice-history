# https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points

class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        x = []
        for p in points:
            x.append(p[0])
        d = -1
        x.sort()
        for i in range(0, len(x)-1):
            if x[i+1]-x[i] > d:
                d = x[i+1]-x[i]
        return d