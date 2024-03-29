class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        for item in set(s):
            if t.count(item) != s.count(item):
                return False

        return True
        