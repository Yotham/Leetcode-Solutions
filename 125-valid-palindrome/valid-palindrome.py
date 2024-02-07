class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        alphaS = ""
        for char in s:
            if char.isalnum():
                alphaS+=char.lower()
        if alphaS == alphaS[::-1]:
            return True
        return False
        