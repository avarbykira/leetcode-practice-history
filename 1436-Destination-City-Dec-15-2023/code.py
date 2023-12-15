class Solution(object):
    def destCity(self, paths):
        startingPoint = []
        endPoint = []
        for item in paths:
            startingPoint.append(item[0])
            endPoint.append(item[1])
        
        for item in endPoint:
            if item not in startingPoint:
                return item