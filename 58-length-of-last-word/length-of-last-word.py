class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        word = s.strip().split(" ")[-1]
        return len(word)
