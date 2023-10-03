class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = ''.join([char for char in s if char.isalpha() or char.isdigit()]).lower()
        return True if s[::-1] == s else False
