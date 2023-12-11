class Solution(object):
    def findSpecialInteger(self, arr):
        l = len(arr)
        step = int(l/4)

        for i in range(0, l):
            if arr[i] == arr[i+step]:
                tar = arr[i]
                break
        
        return tar