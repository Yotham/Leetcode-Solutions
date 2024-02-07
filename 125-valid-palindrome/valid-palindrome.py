class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        alphaS = ''.join([char.lower() for char in s if char.isalnum()])
        if alphaS == alphaS[::-1]:
            return True
        return False
        