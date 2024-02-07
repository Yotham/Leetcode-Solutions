class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        alphaS = ''.join([char.lower() for char in s if char.isalnum()])
        return alphaS == alphaS[::-1]
        