class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(reversed(s.split()))
        return " ".join(s)

        