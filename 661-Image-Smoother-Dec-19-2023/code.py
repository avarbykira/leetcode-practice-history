# Problem Link: https://leetcode.com/problems/image-smoother/

# 1405ms, beats 5% people
# 13.5MB, beats 98% people
import copy
class Solution(object):
    def imageSmoother(self, img):
        ic = copy.deepcopy(img)
        for m in range(0, len(img)):
            for n in range(0, len(img[0])):
                count = 0
                sum = 0
                for i in range(m-1, m+2):
                    for j in range(n-1, n+2):
                        if i in range(0, len(img)) and j in range(0, len(img[0])):
                            count += 1
                            sum += img[i][j]
                ic[m][n] = sum / count
        return ic
    

# refine
# no worth
class Solution(object):
    def imageSmoother(self, img):
        ic = [[0 for _ in range(len(img[0]))] for _ in range(len(img))] # `_` is a common convention in Python for a variable that is not going to be used.
        for m in range(0, len(img)):
            for n in range(0, len(img[0])):
                count = 0
                sum = 0
                for i in range(m-1, m+2):
                    for j in range(n-1, n+2):
                        if i in range(0, len(img)) and j in range(0, len(img[0])):
                            count += 1
                            sum += img[i][j]
                ic[m][n] = sum / count
        return ic
    
"""
The underscore `_` is a common convention in Python for a variable that is not going to be used.
like:
    n = 3
    for _ in range(n):
        print("Hello, world!")
"""