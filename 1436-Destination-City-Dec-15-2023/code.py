# initial commit: 36ms
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

# faster: 30ms   
class Solution(object):
    def destCity(self, paths):
        startingPoint = []
        possiblePoint = []
        for item in paths:
            startingPoint.append(item[0])
            for p in item:
                if p in possiblePoint:
                    possiblePoint.remove(p)
                else:
                    possiblePoint.append(p)
        
        for item in possiblePoint:
            if item not in startingPoint:
                return item
            
# faster? 31ms
class Solution(object):
    def destCity(self, paths):
        startingPoint = []
        possiblePoint = []
        for item in paths:
            startingPoint.append(item[0])
            possiblePoint.append(item[1])
        for p in startingPoint:
            if p in possiblePoint:
                possiblePoint.remove(p)
        return possiblePoint[0]

# same as the first commit: 37ms
class Solution(object):
    def destCity(self, paths):
        startingPoint = []
        possiblePoint = []
        for item in paths:
            startingPoint.append(item[0])
            possiblePoint.append(item[1])
        for p in possiblePoint:
            if p not in startingPoint:
                return p
            
# using set(), 23ms
class Solution(object):
    def destCity(self, paths):
        starts = set()
        destinations = set()
        for start,destination in paths:
            starts.add(start)
            destinations.add(destination)
        
        for destination in destinations:
            if destination not in starts:
                return destination
            
'''
The `set` data structure in Python is implemented as a hash table, which 
provides constant time complexity O(1) for search operations on average.

This means that checking if an item exists in the set takes roughly the same amount of time, 
regardless of the size of the set.
'''
        