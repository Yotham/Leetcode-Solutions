class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = " ".join(s.split())
        split = s.split()
        return len(split[len(split)-1])