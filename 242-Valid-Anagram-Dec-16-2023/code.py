class Solution(object):
    def isAnagram(self, s, t):
        s = "".join(sorted(s))
        t = "".join(sorted(t))
        return s == t
    
# using set()
class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        chars = set(s)  # put everything of s into the set
        # for c in s:
        #     chars.add(c)
        for c in chars:
            if not (c in t and c in s and t.count(c) == s.count(c)):
                return False
        return True