class Solution(object):
    def isPathCrossing(self, path):
        x = 0
        y = 0
        visited = set()
        visited.add((x, y))
        for d in path:
            if d == 'N':
                y += 1
            elif d == 'E':
                x += 1
            elif d == 'S':
                y += -1
            else:
                x += -1
            if (x, y) in visited:
                return True
            visited.add((x, y))
        return False

# Hint: Figure out how to store 2 numbers as 1
class Solution(object):
    def isPathCrossing(self, path):
        x = 0
        y = 0
        visited = set()
        visited.add(x * 114514 + y * 1919810)
        for d in path:
            if d == 'N':
                y += 1
            elif d == 'E':
                x += 1
            elif d == 'S':
                y += -1
            else:
                x += -1
            if (x * 114514 + y * 1919810) in visited:
                return True
            visited.add(x * 114514 + y * 1919810)
        return False