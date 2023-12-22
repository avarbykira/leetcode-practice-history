# https://leetcode.com/problems/maximum-score-after-splitting-a-string

class Solution(object):
    def maxScore(self, s):
        b = -1
        for i in range(1, len(s)):
            ls = s[:i]
            rs = s[i:]
            b = max(b, ls.count('0') + rs.count('1'))
        return b

# abandoned solution    
class Solution(object):
    def maxScore(self, s):
        score = 0
        for i in range(0, len(s)):
            if s[i] == '1':
                score += 1
        temp = score
        for i in range(0, len(s)-2):
            if s[i] == '0':
                temp += 1
            else:
                temp -= 1
            score = max(score, temp)
        return score

# hint: count num of '1's first
# best solution
class Solution(object):
    def maxScore(self, s):
        l = 1 if s[0] == '0' else 0
        r = 1 if s[len(s)-1] == '1' else 0
        oneCount = 0
        shift = 0
        ms = 0
        for i in range(1, len(s)-1):
            if s[i] == '1':
                oneCount += 1
                shift += -1
            else:
                shift += 1
            ms = max(ms, shift)
        return oneCount + ms + l + r