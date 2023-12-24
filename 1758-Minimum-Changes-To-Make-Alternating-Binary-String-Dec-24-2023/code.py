# https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string

class Solution(object):
    def minOperations(self, s):
        s1 = ''.join(['1' if i % 2 == 0 else '0' for i in range(len(s))])
        s2 = ''.join(['1' if i % 2 != 0 else '0' for i in range(len(s))])
        n = int(s, 2)
        n1 = int(s1, 2)
        n2 = int(s2, 2)
        return min(bin(n^n1).count('1'), bin(n^n2).count('1'))

# another approach
class Solution(object):
    def minOperations(self, s):
        s1 = ''.join(['1' if i % 2 == 0 else '0' for i in range(len(s))])
        s2 = ''.join(['1' if i % 2 != 0 else '0' for i in range(len(s))])
        count = 0
        for i in range(0, len(s)):
            if s[i] != s1[i]:
                count += 1
        flag = count
        for i in range(0, len(s)):
            if s[i] != s2[i]:
                count += -1
        return flag if count < 0 else flag-count